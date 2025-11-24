import os
import litellm
from fastapi import HTTPException
import logging

from ..utils.system_prompts import get_system_prompt
from ..utils.code_postprocessor import post_process_code
from ..utils.code_validator import CodeValidator
from ..utils.code_fixer import CodeFixer
# from ..utils.theme_injector import inject_theme_setup # Legacy theme injection removed
from ..inputs.processor import InputProcessor

logger = logging.getLogger(__name__)


def generate_animation_response(
    input_data: str,
    input_type: str = "text",
    category: str = "mathematical",
    max_attempts: int = 3
) -> str:
    """Generate Manim animation code from input with validation and auto-fixing.

    Args:
        input_data (str): User's input (text, URL, or PDF path)
        input_type (str): Type of input ('text', 'url', 'pdf')
        category (str): Animation category (tech_system, product_startup, mathematical)
        max_attempts (int): Maximum generation attempts

    Returns:
        str: Generated Manim animation code (validated and post-processed)

    Raises:
        HTTPException: If code generation fails after all attempts
    """
    validator = CodeValidator()
    fixer = CodeFixer()
    
    # Process input to get the actual prompt text
    try:
        prompt = InputProcessor.process(input_type, input_data)
    except Exception as e:
        logger.error(f"Input processing failed: {e}")
        raise HTTPException(status_code=400, detail=f"Input processing failed: {str(e)}")
    
    primary_model = os.getenv("CODE_GEN_MODEL")
    fallback_model = os.getenv("CODE_GEN_FALLBACK_MODEL", primary_model)
    
    for attempt in range(max_attempts):
        try:
            # Use fallback model on retry attempts
            model = fallback_model if attempt > 0 else primary_model
            
            # Get dynamic system prompt based on category
            system_prompt = get_system_prompt(category)
            
            messages = [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": f"Create a video about:\n\n{prompt}\n\n NOTE!!!: Make sure the objects or text in the generated code are not overlapping at any point in the video. Make sure that each scene is properly cleaned up before transitioning to the next scene.",
                },
            ]
            
            logger.info(f"Generating code (attempt {attempt + 1}/{max_attempts}) with model {model}")
            
            response = litellm.completion(
                model=model, 
                messages=messages, 
                num_retries=2
            )
            
            raw_code = response.choices[0].message.content
            
            # Extract code if wrapped in markdown
            if "```python" in raw_code:
                import re
                match = re.search(r"```python\n(.*?)```", raw_code, re.DOTALL)
                if match:
                    raw_code = match.group(1).strip()
            
            # Post-process the code to fix common issues
            processed_code = post_process_code(raw_code)
            
            # Legacy theme injection removed - themes are now handled by system prompts
            # processed_code = inject_theme_setup(processed_code, category)
            
            # Validate code
            is_valid, errors = validator.validate(processed_code)
            
            if is_valid:
                logger.info("Code validation passed")
                return processed_code
            
            # Try to auto-fix
            logger.warning(f"Code validation failed with {len(errors)} errors, attempting auto-fix")
            fixed_code, is_fixed, remaining_errors = fixer.fix_and_validate(processed_code, max_attempts=2)
            
            if is_fixed:
                logger.info("Code auto-fixed successfully")
                return fixed_code
            
            # If last attempt, return best code we have
            if attempt == max_attempts - 1:
                error_msg = f"Code generation failed after {max_attempts} attempts. Errors: {remaining_errors}"
                logger.error(error_msg)
                raise HTTPException(
                    status_code=500,
                    detail=error_msg
                )
            
            logger.info(f"Retrying code generation (attempt {attempt + 2}/{max_attempts})")
            
        except Exception as e:
            logger.error(f"Error in code generation attempt {attempt + 1}: {str(e)}")
            if attempt == max_attempts - 1:
                raise HTTPException(
                    status_code=500, 
                    detail=f"Failed to generate animation response after {max_attempts} attempts: {str(e)}"
                )
    
    # Should not reach here, but just in case
    raise HTTPException(
        status_code=500,
        detail="Failed to generate valid animation code after all attempts"
    )
