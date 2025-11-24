import os
import hashlib
import json
import logging
import requests
from pathlib import Path
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class SimpleElevenLabsService:
    """
    A simple, robust service for generating voiceovers using ElevenLabs API.
    Bypasses the complex inheritance of manim-voiceover to avoid path type errors.
    """
    
    DEFAULT_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel
    
    VOICE_MAPPING = {
        "Rachel": "21m00Tcm4TlvDq8ikWAM",
        "Adam": "pNInz6obpgDQGcFmaJgB",
        "Bella": "EXAVITQu4vr4xnSDxMaL",
        "Josh": "TxGEqnHWrfWFTfGW9XjX"
    }
    
    BASE_URL = "https://api.elevenlabs.io/v1"
    
    def __init__(self, voice_id: str = DEFAULT_VOICE_ID, cache_dir: Optional[Path] = None):
        # Resolve voice ID if it's a name
        self.voice_id = self.VOICE_MAPPING.get(voice_id, voice_id)
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        if not self.api_key:
            logger.warning("ELEVENLABS_API_KEY not set. Voiceover generation will fail.")
            
        # Use provided cache_dir or default
        if cache_dir:
            self.cache_dir = Path(cache_dir) if not isinstance(cache_dir, Path) else cache_dir
        else:
            self.cache_dir = Path("media/voiceover/elevenlabs")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def generate_from_text(self, text: str, **kwargs) -> Path:
        """
        Generate audio from text and return the path to the audio file.
        Uses a simple hash-based caching mechanism.
        """
        if not text:
            raise ValueError("Text cannot be empty")
            
        # Create a stable hash for the text and voice_id
        content_hash = hashlib.md5(f"{text}-{self.voice_id}".encode("utf-8")).hexdigest()
        output_path = self.cache_dir / f"{content_hash}.mp3"
        
        # Return cached file if it exists
        if output_path.exists() and output_path.stat().st_size > 0:
            logger.info(f"Using cached voiceover for hash {content_hash}")
            return output_path
            
        logger.info(f"Generating new voiceover for: {text[:30]}...")
        
        try:
            if not self.api_key:
                logger.warning("ELEVENLABS_API_KEY missing, falling back to gTTS")
                return self._generate_with_gtts(text)

            # Call ElevenLabs API
            url = f"{self.BASE_URL}/text-to-speech/{self.voice_id}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.api_key
            }
            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75
                }
            }

            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            
            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        
            logger.info(f"Voiceover saved to {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"ElevenLabs generation failed: {str(e)}. Falling back to gTTS.")
            return self._generate_with_gtts(text)

    def _generate_with_gtts(self, text: str) -> Path:
        """
        Fallback generation using Google Text-to-Speech (free).
        """
        try:
            from gtts import gTTS
            
            # Use a separate cache for gTTS to avoid hash collisions if we switch back
            gtts_cache_dir = Path("media/voiceover/gtts")
            gtts_cache_dir.mkdir(parents=True, exist_ok=True)
            
            content_hash = hashlib.md5(text.encode("utf-8")).hexdigest()
            output_path = gtts_cache_dir / f"{content_hash}.mp3"
            
            if output_path.exists() and output_path.stat().st_size > 0:
                logger.info(f"Using cached gTTS voiceover for hash {content_hash}")
                return output_path
                
            logger.info(f"Generating gTTS fallback for: {text[:30]}...")
            tts = gTTS(text=text, lang='en')
            tts.save(str(output_path))
            
            logger.info(f"gTTS voiceover saved to {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"gTTS fallback failed: {str(e)}")
            raise RuntimeError(f"Voiceover generation failed (ElevenLabs and gTTS): {str(e)}")
