import os
import litellm
from fastapi import HTTPException

from ..utils.system_prompts import MANIM_SYSTEM_PROMPT


def generate_animation_response(prompt: str) -> str:
    """Generate Manim animation code from a text prompt.

    Args:
        prompt (str): User's request for an animation

    Returns:
        str: Generated Manim animation code

    Raises:
        HTTPException: If code generation fails
    """

    try:
        messages = [
            {
                "role": "system",
                "content": MANIM_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"{prompt}\n\n NOTE!!!: Make sure the objects or text in the generated code are not overlapping at any point in the video. Make sure that each scene is properly cleaned up before transitioning to the next scene.",
            },
        ]
        
        response = litellm.completion(
            model=os.getenv("CODE_GEN_MODEL"), 
            messages=messages, 
            num_retries=2
        )
        
        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to generate animation response: {str(e)}"
        )
