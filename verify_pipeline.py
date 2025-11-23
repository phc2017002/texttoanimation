import asyncio
import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from manimator.utils.visual_analyzer import create_visual_analyzer
from api_server import Config

async def test_pipeline():
    print("🚀 Starting Pipeline Verification Test...")
    
    # 1. Render the "bad" scene first
    print("\n🎥 Rendering 'bad' scene (reproduce_particle_box.py)...")
    # Use python -m manim to ensure we use the installed package
    import sys
    cmd = f"{sys.executable} -m manim -pqh reproduce_particle_box.py ParticleInABox"
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    
    print(f"STDOUT: {stdout.decode()}")
    print(f"STDERR: {stderr.decode()}")
    
    if process.returncode != 0:
        print(f"❌ Rendering failed with code {process.returncode}")
        return

    # Find the video
    video_dir = Path("media/videos/reproduce_particle_box/1080p60")
    video_files = list(video_dir.glob("*.mp4"))
    if not video_files:
        print("❌ No video file found!")
        return
    
    video_path = video_files[0]
    print(f"✅ Video rendered: {video_path}")
    
    # 2. Run Visual Analyzer
    print("\n👁️ Running Visual Layout Analyzer (Gemini 3.0 Pro Preview)...")
    analyzer = create_visual_analyzer()
    
    # Read original code
    with open("reproduce_particle_box.py", "r") as f:
        original_code = f.read()
        
    # Analyze and Fix
    print("   (This may take a moment as it calls Gemini and then Claude...)")
    fixed_code, report = analyzer.analyze_and_fix(
        original_code,
        video_path,
        max_iterations=1
    )
    
    # 3. Print Results
    print("\n📊 Analysis Report (Gemini):")
    print(json.dumps(report, indent=2))
    
    # Save report to file for inspection
    with open("verification_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("💾 Saved analysis report to 'verification_report.json'")
    
    if report.get("has_issues"):
        print("\n✅ Issues DETECTED by Gemini!")
    else:
        print("\n❌ Gemini did NOT detect issues (Unexpected for this test case).")
        
    print("\n🛠️ Fixed Code (Claude 4.5 Sonnet):")
    print("-" * 40)
    print(fixed_code)
    print("-" * 40)
    
    if fixed_code != original_code:
        print("\n✅ Code was MODIFIED by Claude!")
        
        # Save fixed code
        with open("reproduce_issue_fixed.py", "w") as f:
            f.write(fixed_code)
        print("💾 Saved fixed code to 'reproduce_issue_fixed.py'")
        
        # Optional: Render fixed code
        print("\n🎥 Rendering FIXED scene...")
        cmd_fix = "manim -pql reproduce_issue_fixed.py CircularConcept"
        process_fix = await asyncio.create_subprocess_shell(
            cmd_fix,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await process_fix.communicate()
        print("✅ Fixed scene rendered!")
        
    else:
        print("\n⚠️ Code was NOT modified (Claude didn't suggest changes or Gemini found no issues).")

if __name__ == "__main__":
    asyncio.run(test_pipeline())
