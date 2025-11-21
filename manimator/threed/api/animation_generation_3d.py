"""
3D Animation Code Generation

Generates Manim code for 3D animations using LLM.
"""

import os
import re
from typing import Optional
from fastapi import HTTPException
import litellm

from .prompts_3d import get_3d_system_prompt, get_3d_examples, SYSTEM_PROMPT_3D
from manimator.utils.code_postprocessor import post_process_code


def generate_3d_animation_response(
    user_prompt: str,
    model: Optional[str] = None,
    include_examples: bool = True
) -> str:
    """
    Generate 3D Manim animation code from a text prompt.
    
    Args:
        user_prompt: User's request for a 3D animation
        model: LiteLLM model to use (defaults to CODE_GEN_MODEL env var)
        include_examples: Whether to include example code in the system prompt
    
    Returns:
        Generated 3D Manim animation code (post-processed)
    
    Raises:
        HTTPException: If code generation fails
    """
    try:
        # Build system prompt
        system_prompt = get_3d_system_prompt()
        
        if include_examples:
            examples = get_3d_examples()
            examples_text = "\n\n".join([
                f"## {name.upper()} EXAMPLE\n{code}"
                for name, code in examples.items()
            ])
            system_prompt += f"\n\nHERE ARE SOME EXAMPLES:\n\n{examples_text}"
        
        # Build messages
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"""Create a complete, runnable Manim 3D animation for the following request:

{user_prompt}

Requirements:
1. Use ThreeDScene as base class
2. Include voiceover narration
3. Set appropriate camera angles
4. Make it educational and visually appealing
5. Include mathematical equations if relevant
6. Use smooth animations and camera movements
7. Aim for 2-5 minutes duration (or as specified)

Generate ONLY the Python code, nothing else."""}
        ]
        
        # Use specified model or default
        if model is None:
            model = os.getenv("CODE_GEN_MODEL")
        
        # Generate code
        response = litellm.completion(
            model=model,
            messages=messages,
            num_retries=2
        )
        
        raw_code = response.choices[0].message.content
        
        # Extract code if wrapped in markdown
        pattern = r'```python\n(.*?)```'
        match = re.search(pattern, raw_code, re.DOTALL)
        
        if match:
            code = match.group(1)
        else:
            code = raw_code
        
        # Post-process the code to fix common issues
        processed_code = post_process_code(code)
        
        return processed_code
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate 3D animation: {str(e)}"
        )


def generate_3d_animation_with_category(
    user_prompt: str,
    category: str,
    model: Optional[str] = None
) -> str:
    """
    Generate 3D animation code with a specific STEM category focus.
    
    Args:
        user_prompt: User's description
        category: One of 'mathematical', 'scientific', 'geometric', 'data'
        model: LLM model to use
        
    Returns:
        Generated Python code
    """
    category_prompts = {
        "mathematical": "Focus on mathematical accuracy and clear visualization of mathematical concepts.",
        "scientific": "Focus on scientific accuracy, realistic models, and clear explanations.",
        "geometric": "Focus on geometric properties, transformations, and spatial relationships.",
        "data": "Focus on clear data representation, appropriate chart types, and data-driven insights."
    }
    
    enhanced_prompt = f"""{user_prompt}

CATEGORY: {category.upper()}
{category_prompts.get(category, '')}
"""
    
    return generate_3d_animation_response(enhanced_prompt, model=model)
