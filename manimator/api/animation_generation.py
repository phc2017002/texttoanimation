import os
import litellm
from fastapi import HTTPException

from ..utils.system_prompts import get_system_prompt
from ..utils.code_postprocessor import post_process_code


def generate_animation_response(prompt: str, category: str = "mathematical") -> str:
    """Generate Manim animation code from a text prompt.

    Args:
        prompt (str): User's request for an animation

    Returns:
        str: Generated Manim animation code (post-processed)

    Raises:
        HTTPException: If code generation fails
    """

    try:
        system_prompt = get_system_prompt(category)
        messages = [
            {
                "role": "system",
                "content": system_prompt,
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
        
        raw_code = response.choices[0].message.content
        
        # Post-process the code to fix common issues
        processed_code = post_process_code(raw_code)
        
        return processed_code
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to generate animation response: {str(e)}"
        )
