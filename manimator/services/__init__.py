"""
Services module for Manimator

Includes ElevenLabs TTS Service and Web Scraper
"""

# Lazy imports to avoid dependency issues
def __getattr__(name):
    if name == "ElevenLabsService":
        from .elevenlabs_service import ElevenLabsService
        return ElevenLabsService
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

__all__ = ["ElevenLabsService"]
