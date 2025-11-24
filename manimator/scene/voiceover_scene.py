import logging
from pathlib import Path
from manim import Scene
from manimator.services.voiceover import SimpleElevenLabsService

logger = logging.getLogger(__name__)

class VoiceoverTracker:
    """
    Simple tracker to mimic the behavior of manim-voiceover's tracker.
    Used in the 'with self.voiceover(...) as tracker:' context.
    """
    def __init__(self, duration: float):
        self.duration = duration

class VoiceoverScene(Scene):
    """
    A robust base class for scenes with voiceovers.
    Replaces the fragile manim-voiceover library with a direct implementation.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speech_service = SimpleElevenLabsService()
        
    def set_speech_service(self, service):
        """
        Set the speech service. Kept for compatibility with generated code patterns,
        but primarily we use the internal SimpleElevenLabsService.
        """
        if isinstance(service, SimpleElevenLabsService):
            self.speech_service = service
        # If it's the old service type, we ignore it or log a warning, 
        # but for now we assume generated code will be updated to use the new service or 
        # we just use our default one if they pass something else.
        
    def voiceover(self, text: str):
        """
        Context manager for voiceovers.
        Generates audio, adds it to the scene, and handles timing.
        """
        # Generate audio
        audio_path = self.speech_service.generate_from_text(text)
        
        # Add audio to scene
        self.add_sound(str(audio_path))
        
        # Calculate duration (approximate or exact if we could read metadata)
        # For now, we rely on Manim's add_sound to handle playback.
        # But we need to know how long to wait.
        
        # We need to get the duration of the audio file.
        # Since we want to avoid heavy dependencies like pydub/sox if possible,
        # we can try a lightweight approach or just use mutagen if available.
        # Given the environment has 'manim', it likely has tools to read audio duration.
        
        duration = self._get_audio_duration(audio_path)
        
        return _VoiceoverContext(self, duration)

    def _get_audio_duration(self, file_path: Path) -> float:
        """
        Get duration of mp3 file.
        Uses mutagen if available (installed by manim-voiceover), otherwise estimates.
        """
        try:
            from mutagen.mp3 import MP3
            audio = MP3(file_path)
            return audio.info.length
        except ImportError:
            logger.warning("mutagen not found, estimating duration based on file size")
            # Rough estimate: 1MB ~ 1 minute for 128kbps mp3
            # This is a fallback and might be inaccurate
            size_bytes = file_path.stat().st_size
            # 128 kbps = 16 KB/s
            return size_bytes / 16000.0
        except Exception as e:
            logger.error(f"Error reading audio duration: {e}")
            return 2.0 # Safe default fallback

class _VoiceoverContext:
    """Context manager helper"""
    def __init__(self, scene: Scene, duration: float):
        self.scene = scene
        self.duration = duration
        self.tracker = VoiceoverTracker(duration)
        
    def __enter__(self):
        # Capture start time from the renderer
        # This allows us to track how much time passes during the animations inside the block
        self.start_time = self.scene.renderer.time
        return self.tracker
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            return  # Don't wait if there was an exception
            
        # Calculate how much time passed during the block
        current_time = self.scene.renderer.time
        elapsed = current_time - self.start_time
        
        # Calculate remaining duration of the audio
        remaining = self.duration - elapsed
        
        # If the animations were shorter than the audio, wait for the rest
        if remaining > 0:
            # Add a small buffer to ensure clean separation
            self.scene.wait(remaining)
            
        # Optional: Add a tiny pause between voiceovers for better pacing
        # self.scene.wait(0.1)
