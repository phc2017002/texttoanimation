"""
Unified FastAPI Video Generation Server
Supports text prompts, PDFs, and URLs for all animation categories.
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Literal, Union
from enum import Enum
import uuid
import os
import json
import subprocess
import shutil
from datetime import datetime
from pathlib import Path
import asyncio
import logging
import base64

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

from manimator.api.animation_generation import generate_animation_response
# from manimator.api.input_processor import process_input

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("api_server_unified")

# ============================================================================
# Configuration
# ============================================================================

class Config:
    """Application configuration"""
    BASE_DIR = Path(__file__).parent
    JOBS_DIR = BASE_DIR / "jobs"
    VIDEOS_DIR = BASE_DIR / "media" / "videos"
    MAX_JOB_AGE_DAYS = 7
    
    # Ensure directories exist
    JOBS_DIR.mkdir(exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# Models
# ============================================================================

class JobStatus(str, Enum):
    """Job status enumeration"""
    PENDING = "pending"
    GENERATING_CODE = "generating_code"
    RENDERING = "rendering"
    COMPLETED = "completed"
    FAILED = "failed"


class QualityLevel(str, Enum):
    """Video quality levels"""
    LOW = "low"       # 480p15
    MEDIUM = "medium" # 720p30
    HIGH = "high"     # 1080p60
    ULTRA = "ultra"   # 4K60


class AnimationCategory(str, Enum):
    """Animation categories"""
    TECH_SYSTEM = "tech_system"
    PRODUCT_STARTUP = "product_startup"
    MATHEMATICAL = "mathematical"


QUALITY_FLAGS = {
    QualityLevel.LOW: "-pql",
    QualityLevel.MEDIUM: "-pqm",
    QualityLevel.HIGH: "-pqh",
    QualityLevel.ULTRA: "-pqk",
}


class VideoRequest(BaseModel):
    """Request model for video generation"""
    input_type: Literal["text", "pdf", "url"] = Field(..., description="Type of input")
    input_data: Union[str, bytes] = Field(..., description="Input data (text prompt, base64 PDF, or URL)")
    quality: QualityLevel = Field(default=QualityLevel.HIGH, description="Video quality level")
    category: AnimationCategory = Field(default=AnimationCategory.MATHEMATICAL, description="Animation category")
    scene_name: Optional[str] = Field(default=None, description="Custom scene class name")
    
    class Config:
        json_schema_extra = {
            "example": {
                "input_type": "text",
                "input_data": "Explain how a distributed system handles requests",
                "quality": "high",
                "category": "tech_system"
            }
        }


class JobResponse(BaseModel):
    """Response model for job creation"""
    job_id: str
    status: JobStatus
    message: str
    created_at: str


class JobStatusResponse(BaseModel):
    """Response model for job status"""
    job_id: str
    status: JobStatus
    category: str
    progress: Dict[str, Any]
    created_at: str
    updated_at: str
    error: Optional[str] = None
    video_url: Optional[str] = None
    duration: Optional[float] = None


# ============================================================================
# Job Manager
# ============================================================================

class JobManager:
    """Manages video generation jobs"""
    
    def __init__(self):
        self.jobs: Dict[str, Dict] = {}
        self._load_existing_jobs()
        self._cleanup_task = None
    
    def _load_existing_jobs(self):
        """Load existing jobs from disk"""
        for job_file in Config.JOBS_DIR.glob("*.json"):
            try:
                with open(job_file) as f:
                    job_data = json.load(f)
                    self.jobs[job_data["job_id"]] = job_data
            except Exception as e:
                logger.error(f"Error loading job {job_file}: {e}")
    
    def create_job(
        self,
        input_type: str,
        input_data: Union[str, bytes],
        quality: QualityLevel,
        category: AnimationCategory,
        scene_name: Optional[str] = None
    ) -> str:
        """Create a new job"""
        job_id = str(uuid.uuid4())
        
        if not scene_name:
            scene_name = f"Scene_{uuid.uuid4().hex[:8]}"
        
        job_data = {
            "job_id": job_id,
            "status": JobStatus.PENDING,
            "input_type": input_type,
            "quality": quality,
            "category": category.value,
            "scene_name": scene_name,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "progress": {
                "stage": "queued",
                "percentage": 0,
                "message": "Job queued for processing"
            },
            "error": None,
            "video_path": None,
            "code_path": None,
        }
        
        # Store input data (truncate if too long for display)
        if input_type == "text":
            job_data["input_preview"] = str(input_data)[:200] + "..." if len(str(input_data)) > 200 else str(input_data)
        elif input_type == "url":
            job_data["input_preview"] = str(input_data)
        else:
            job_data["input_preview"] = "[PDF file]"
        
        self.jobs[job_id] = job_data
        self._save_job(job_id)
        return job_id
    
    def update_job(self, job_id: str, **kwargs):
        """Update job data"""
        if job_id not in self.jobs:
            return
        
        self.jobs[job_id].update(kwargs)
        self.jobs[job_id]["updated_at"] = datetime.now().isoformat()
        self._save_job(job_id)
    
    def get_job(self, job_id: str) -> Optional[Dict]:
        """Get job by ID"""
        return self.jobs.get(job_id)
    
    def _save_job(self, job_id: str):
        """Save job to disk"""
        # Ensure directory exists
        Config.JOBS_DIR.mkdir(parents=True, exist_ok=True)
        job_file = Config.JOBS_DIR / f"{job_id}.json"
        with open(job_file, 'w') as f:
            json.dump(self.jobs[job_id], f, indent=2)
    
    def list_jobs(self, limit: int = 50) -> List[Dict]:
        """List recent jobs"""
        jobs = sorted(
            self.jobs.values(),
            key=lambda x: x["created_at"],
            reverse=True
        )
        return jobs[:limit]
    
    def start_periodic_cleanup(self):
        """Start periodic cleanup task (call this after event loop is running)"""
        if self._cleanup_task is None:
            self._cleanup_task = asyncio.create_task(self._periodic_cleanup())
    
    async def _periodic_cleanup(self):
        """Periodic cleanup of old jobs and voiceover cache"""
        import time
        # Wait a bit before starting cleanup
        await asyncio.sleep(60)
        while True:
            try:
                await asyncio.sleep(3600)  # Run every hour
                await self._cleanup_old_jobs()
                await self._cleanup_old_voiceovers()
            except Exception as e:
                logger.warning(f"Periodic cleanup error: {e}")
    
    async def _cleanup_old_jobs(self):
        """Remove old job files and their associated data"""
        cutoff_date = datetime.now().timestamp() - (Config.MAX_JOB_AGE_DAYS * 24 * 3600)
        removed_count = 0
        
        for job_id, job_data in list(self.jobs.items()):
            try:
                job_time = datetime.fromisoformat(job_data["created_at"]).timestamp()
                if job_time < cutoff_date:
                    # Remove job file
                    job_file = Config.JOBS_DIR / f"{job_id}.json"
                    if job_file.exists():
                        job_file.unlink()
                    
                    # Remove from memory
                    del self.jobs[job_id]
                    removed_count += 1
            except Exception as e:
                logger.warning(f"Error cleaning up job {job_id[:8]}: {e}")
        
        if removed_count > 0:
            logger.info(f"🧹 Cleaned up {removed_count} old jobs")
    
    async def _cleanup_old_voiceovers(self):
        """Clean up old voiceover cache files (keep recent ones)"""
        import time
        try:
            # Clean both ElevenLabs and gTTS cache
            for service_dir in ["elevenlabs", "gtts"]:
                voiceover_dir = Config.BASE_DIR / "media" / "voiceover" / service_dir
                if not voiceover_dir.exists():
                    continue
                
                # Keep voiceover files from last 7 days
                cutoff_time = time.time() - (7 * 24 * 3600)
                removed_count = 0
                
                for voice_file in voiceover_dir.glob("*.mp3"):
                    try:
                        if voice_file.stat().st_mtime < cutoff_time:
                            voice_file.unlink()
                            removed_count += 1
                    except Exception:
                        pass
                
                if removed_count > 0:
                    logger.info(f"🧹 Cleaned up {removed_count} old {service_dir} voiceover files")
        except Exception as e:
            logger.warning(f"Error cleaning up voiceovers: {e}")


# ============================================================================
# Video Generator
# ============================================================================

class VideoGenerator:
    """Handles video generation workflow"""
    
    def __init__(self, job_manager: JobManager):
        self.job_manager = job_manager
    
    async def generate_video(self, job_id: str):
        """Generate video for a job"""
        job = self.job_manager.get_job(job_id)
        if not job:
            return
        
        logger.info(f"🎬 Starting video generation for job {job_id[:8]}...")
        
        try:
            # Stage 2: Generate Manim code
            logger.info(f"🤖 Generating Manim code for job {job_id[:8]}...")
            self.job_manager.update_job(
                job_id,
                status=JobStatus.GENERATING_CODE,
                progress={
                    "stage": "generating_code",
                    "percentage": 30,
                    "message": "Generating Manim code using AI..."
                }
            )
            
            # Pass raw input to generation function which now handles processing
            code = generate_animation_response(
                input_data=job.get("input_data", ""),
                input_type=job["input_type"],
                category=job["category"]
            )
            
            logger.info(f"✅ Code generation complete for job {job_id[:8]}...")
            
            # Save code
            code_file = Config.BASE_DIR / f"scene_{job_id}.py"
            with open(code_file, 'w') as f:
                f.write(code)
            
            logger.info(f"💾 Code saved to {code_file.name}")
            
            # Ensure voiceover directories exist
            voiceover_dir = Config.BASE_DIR / "media" / "voiceover"
            (voiceover_dir / "elevenlabs").mkdir(parents=True, exist_ok=True)
            (voiceover_dir / "gtts").mkdir(parents=True, exist_ok=True)
            
            self.job_manager.update_job(
                job_id,
                code_path=str(code_file),
                progress={
                    "stage": "code_generated",
                    "percentage": 50,
                    "message": "Code generated successfully"
                }
            )
            
            # Stage 3: Render video
            logger.info(f"🎥 Starting Manim rendering for job {job_id[:8]}...")
            self.job_manager.update_job(
                job_id,
                status=JobStatus.RENDERING,
                progress={
                    "stage": "rendering",
                    "percentage": 60,
                    "message": "Rendering video (this may take several minutes)..."
                }
            )
            
            video_path = await self._render_video(
                code_file,
                job["scene_name"],
                QualityLevel(job["quality"])
            )
            
            logger.info(f"✅ Video rendering complete for job {job_id[:8]}...")
            
            # Stage 4: Complete
            self.job_manager.update_job(
                job_id,
                status=JobStatus.COMPLETED,
                video_path=str(video_path),
                progress={
                    "stage": "completed",
                    "percentage": 100,
                    "message": "Video generation completed successfully!"
                }
            )
            
            # Stage 5: Cleanup intermediate files in background
            asyncio.create_task(self._cleanup_intermediate_files(job_id, code_file, video_path))
            
        except Exception as e:
            logger.error(f"❌ Error generating video for job {job_id[:8]}: {str(e)}")
            self.job_manager.update_job(
                job_id,
                status=JobStatus.FAILED,
                error=str(e),
                progress={
                    "stage": "failed",
                    "percentage": 0,
                    "message": f"Error: {str(e)}"
                }
            )
    
    async def _render_video(self, code_file: Path, scene_name: str, quality: QualityLevel) -> Path:
        """Render Manim scene to video"""
        quality_flag = QUALITY_FLAGS[quality]
        
        # Ensure ALL media directories exist before rendering
        media_dir = Config.BASE_DIR / "media"
        voiceover_dir = media_dir / "voiceover" / "elevenlabs"
        voiceover_dir.mkdir(parents=True, exist_ok=True)
        
        # Also create gTTS cache directory in case of fallback
        gtts_dir = media_dir / "voiceover" / "gtts"
        gtts_dir.mkdir(parents=True, exist_ok=True)
        
        # Create videos directory structure
        Config.VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
        
        cmd = [
            "manim",
            quality_flag,
            "--media_dir",
            str(Config.BASE_DIR / "media"),
            str(code_file),
            scene_name,
        ]
        
        # Set working directory to base dir to ensure relative paths work
        env = os.environ.copy()
        # Set MEDIA_DIR as absolute path to help voiceover services find cache directory
        env["MEDIA_DIR"] = str(media_dir.resolve())

        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(Config.BASE_DIR),
            env=env
        )
        
        stdout, stderr = await process.communicate()
        
        if process.returncode != 0:
            error_output = stderr.decode()[-500:] if stderr else "Unknown error"
            raise Exception(f"Manim rendering failed: {error_output}")
        
        # Find generated video
        quality_dir = {
            QualityLevel.LOW: "480p15",
            QualityLevel.MEDIUM: "720p30",
            QualityLevel.HIGH: "1080p60",
            QualityLevel.ULTRA: "2160p60"
        }[quality]
        
        video_dir = Config.VIDEOS_DIR / code_file.stem / quality_dir
        video_files = list(video_dir.glob("*.mp4"))
        
        if not video_files:
            raise Exception(f"No video file found in {video_dir}")
        
        video_path = video_files[0]
        logger.info(f"📹 Found video: {video_path.name}")
        
        return video_path
    
    async def _cleanup_intermediate_files(self, job_id: str, code_file: Path, final_video_path: Path):
        """
        Clean up intermediate files in background after video is successfully created.
        Removes: scene code files, partial videos, voiceover files (keeps final video).
        
        Args:
            job_id: Job ID
            code_file: Path to generated scene code file
            final_video_path: Path to final rendered video (keep this)
        """
        try:
            logger.info(f"🧹 Starting cleanup for job {job_id[:8]}...")
            
            # 1. Remove scene code file
            if code_file.exists():
                try:
                    code_file.unlink()
                    logger.info(f"   ✅ Removed scene code: {code_file.name}")
                except Exception as e:
                    logger.warning(f"   ⚠️  Could not remove scene code: {e}")
            
            # 2. Remove partial video files (keep only final video)
            # Find all video files in the scene directory
            scene_video_dir = Config.VIDEOS_DIR / code_file.stem
            if scene_video_dir.exists():
                # Keep only the final video, remove all other quality versions and partial files
                final_video_name = final_video_path.name
                for quality_dir in scene_video_dir.iterdir():
                    if quality_dir.is_dir():
                        for video_file in quality_dir.glob("*.mp4"):
                            # Keep only the final video file
                            if video_file.name != final_video_name:
                                try:
                                    video_file.unlink()
                                    logger.info(f"   ✅ Removed partial video: {video_file.name}")
                                except Exception as e:
                                    logger.warning(f"   ⚠️  Could not remove partial video: {e}")
                        
                        # Remove partial movie files directory if exists
                        partial_dir = quality_dir / "partial_movie_files"
                        if partial_dir.exists():
                            try:
                                shutil.rmtree(partial_dir)
                                logger.info(f"   ✅ Removed partial movie files directory")
                            except Exception as e:
                                logger.warning(f"   ⚠️  Could not remove partial files: {e}")
            
            # 3. Remove voiceover files for this job (they're cached, so safe to remove)
            # Voiceover files are cached by text hash, so we can't easily identify job-specific ones
            # Instead, we'll clean up old voiceover files periodically (not per-job)
            # This is handled by a separate cleanup task
            
            # 4. Remove any temporary files in media directory for this scene
            scene_media_dir = Config.BASE_DIR / "media" / "videos" / code_file.stem
            if scene_media_dir.exists():
                # Remove text SVGs, images, etc. but keep the final video directory structure
                for item in scene_media_dir.iterdir():
                    if item.is_file() and item.suffix in ['.svg', '.png', '.jpg', '.txt', '.srt']:
                        try:
                            item.unlink()
                            logger.info(f"   ✅ Removed temporary file: {item.name}")
                        except Exception as e:
                            logger.warning(f"   ⚠️  Could not remove temp file: {e}")
            
            logger.info(f"✅ Cleanup completed for job {job_id[:8]}")
            
        except Exception as e:
            # Don't fail the job if cleanup fails
            logger.warning(f"⚠️  Cleanup error for job {job_id[:8]}: {e}")


# ============================================================================
# FastAPI Application
# ============================================================================

app = FastAPI(
    title="Unified Manim Video Generation API",
    description="Generate educational animation videos from text, PDFs, or URLs",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize managers
job_manager = JobManager()
video_generator = VideoGenerator(job_manager)


@app.on_event("startup")
async def startup_event():
    """Startup event - initialize background tasks"""
    job_manager.start_periodic_cleanup()
    logger.info("✅ Background cleanup tasks started")


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "name": "Unified Manim Video Generation API",
        "version": "2.0.0",
        "description": "Supports text prompts, PDFs, and URLs",
        "categories": ["tech_system", "product_startup", "mathematical"],
        "input_types": ["text", "pdf", "url"],
        "endpoints": {
            "docs": "/docs",
            "create_video": "POST /api/videos",
            "get_status": "GET /api/jobs/{job_id}",
            "download_video": "GET /api/videos/{job_id}",
            "list_jobs": "GET /api/jobs"
        }
    }


@app.post("/api/videos", response_model=JobResponse)
async def create_video(request: VideoRequest, background_tasks: BackgroundTasks):
    """
    Create a new video generation job
    
    Supports three input types:
    - text: Plain text prompt
    - pdf: Base64 encoded PDF file
    - url: URL to scrape content from
    """
    # Store input data in job
    input_data = request.input_data
    
    # Create job
    job_id = job_manager.create_job(
        input_type=request.input_type,
        input_data=input_data,
        quality=request.quality,
        category=request.category,
        scene_name=request.scene_name
    )
    
    # Store full input data for processing
    job_manager.jobs[job_id]["input_data"] = input_data
    
    logger.info(f"📝 New job created: {job_id} (type: {request.input_type}, category: {request.category})")
    
    # Start generation in background
    background_tasks.add_task(video_generator.generate_video, job_id)
    
    return JobResponse(
        job_id=job_id,
        status=JobStatus.PENDING,
        message="Job created successfully. Video generation started.",
        created_at=datetime.now().isoformat()
    )


@app.get("/api/jobs/{job_id}", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    """Get the status of a video generation job"""
    job = job_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    video_url = None
    duration = None
    
    if job["status"] == JobStatus.COMPLETED and job.get("video_path"):
        video_url = f"/api/videos/{job_id}"
        
        # Get video duration if available
        try:
            video_path = Path(job["video_path"])
            if video_path.exists():
                result = subprocess.run(
                    ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "default=noprint_wrappers=1:nokey=1", str(video_path)],
                    capture_output=True,
                    text=True
                )
                duration = float(result.stdout.strip())
        except:
            pass
    
    return JobStatusResponse(
        job_id=job_id,
        status=job["status"],
        category=job["category"],
        progress=job["progress"],
        created_at=job["created_at"],
        updated_at=job["updated_at"],
        error=job.get("error"),
        video_url=video_url,
        duration=duration
    )


@app.get("/api/videos/{job_id}")
async def download_video(job_id: str):
    """Download the generated video file"""
    job = job_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job["status"] != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Video not ready. Status: {job['status']}"
        )
    
    video_path = Path(job["video_path"])
    if not video_path.exists():
        raise HTTPException(status_code=404, detail="Video file not found")
    
    return FileResponse(
        video_path,
        media_type="video/mp4",
        filename=f"animation_{job_id[:8]}.mp4"
    )


@app.get("/api/jobs")
async def list_jobs(limit: int = 50):
    """List recent jobs"""
    jobs = job_manager.list_jobs(limit)
    return {"jobs": jobs, "total": len(jobs)}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "2.0.0",
        "jobs": {
            "total": len(job_manager.jobs),
            "pending": sum(1 for j in job_manager.jobs.values() if j["status"] == JobStatus.PENDING),
            "processing": sum(1 for j in job_manager.jobs.values() if j["status"] in [JobStatus.GENERATING_CODE, JobStatus.RENDERING]),
            "completed": sum(1 for j in job_manager.jobs.values() if j["status"] == JobStatus.COMPLETED),
            "failed": sum(1 for j in job_manager.jobs.values() if j["status"] == JobStatus.FAILED)
        }
    }


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting Unified Manim Video Generation API Server...")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔍 ReDoc Documentation: http://localhost:8000/redoc")
    print("✨ Supports: Text, PDF, and URL inputs")
    print("🎨 Categories: Tech System, Product Startup, Mathematical")
    
    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )
