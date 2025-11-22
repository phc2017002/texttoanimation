"""
Code Post-Processor for Manim

Fixes common issues in AI-generated Manim code, particularly around
SurroundingRectangle with indexed MathTex elements.
"""

import re
from typing import List


def fix_surrounding_rectangles(code: str) -> str:
    """
    Fix or remove SurroundingRectangle calls that use indexed access to MathTex.
    
    Problem: AI often generates code like:
        SurroundingRectangle(equation[0][5], ...)
    
    This doesn't work reliably because MathTex indexing is unpredictable.
    
    Solution: Comment out these problematic lines with an explanation.
    
    Args:
        code: Raw generated Manim code
    
    Returns:
        Fixed code with problematic SurroundingRectangle calls commented out
    """
    lines = code.split('\n')
    fixed_lines = []
    skip_next = False  # Initialize before the loop
    
    for line in lines:
        # Pattern: SurroundingRectangle with indexed access like equation[0][5]
        # Matches: SurroundingRectangle(something[X][Y], ...) or SurroundingRectangle(something[X:Y], ...)
        if 'SurroundingRectangle(' in line:
            # Check if it has indexed or sliced access
            # Pattern: variable[number] or variable[number:number] inside SurroundingRectangle()
            if re.search(r'SurroundingRectangle\([^,\)]*\[\d+\]', line) or \
               re.search(r'SurroundingRectangle\([^,\)]*\[\d+:\d*\]', line):
                # Comment out the problematic line
                indent = len(line) - len(line.lstrip())
                commented = ' ' * indent + '# ' + line.lstrip() + '  # Auto-disabled: indexed SurroundingRectangle'
                fixed_lines.append(commented)
                
                # Also comment out the related play/create commands on next few lines
                # Mark that we need to skip related animations
                skip_next = True
            else:
                fixed_lines.append(line)
                skip_next = False
        elif skip_next and ('self.play(Create(' in line or 'self.play(Write(' in line):
            # Check if this play command is related to the rectangle we just commented
            if '_box' in line or '_label' in line:
                indent = len(line) - len(line.lstrip())
                commented = ' ' * indent + '# ' + line.lstrip() + '  # Auto-disabled: related to indexed rectangle'
                fixed_lines.append(commented)
            else:
                fixed_lines.append(line)
                skip_next = False
        elif skip_next and 'FadeOut(' in line:
            # Also comment out fadeout of the disabled rectangles
            if '_box' in line or '_label' in line:
                indent = len(line) - len(line.lstrip())
                commented = ' ' * indent + '# ' + line.lstrip() + '  # Auto-disabled: related to indexed rectangle'
                fixed_lines.append(commented)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
            if skip_next:
                # Stop skipping after a few lines
                skip_next = False
    
    return '\n'.join(fixed_lines)


def remove_problematic_indexing(code: str) -> str:
    """
    More aggressive approach: Remove entire blocks that use indexed MathTex highlighting.
    
    This removes the entire voiceover block if it contains indexed SurroundingRectangle.
    """
    # For now, use the commenting approach which is safer
    return fix_surrounding_rectangles(code)


def fix_undefined_colors(code: str) -> str:
    """
    Fix undefined color constants by replacing them with valid Manim colors.
    
    Common issues:
    - ORANGE_A, ORANGE_B, etc. -> ORANGE
    - RED_A, RED_B, etc. -> RED
    - Similar patterns for other colors
    
    Args:
        code: Raw generated code
    
    Returns:
        Code with undefined colors replaced
    """
    # Color mappings: undefined variants -> standard colors
    color_replacements = {
        # Orange variants
        r'\bORANGE_[A-Z]\b': 'ORANGE',
        # Red variants
        r'\bRED_[A-Z]\b': 'RED',
        # Blue variants
        r'\bBLUE_[A-Z]\b': 'BLUE',
        # Green variants
        r'\bGREEN_[A-Z]\b': 'GREEN',
        # Yellow variants
        r'\bYELLOW_[A-Z]\b': 'YELLOW',
        # Purple variants
        r'\bPURPLE_[A-Z]\b': 'PURPLE',
        # Pink variants
        r'\bPINK_[A-Z]\b': 'PINK',
        # Teal variants
        r'\bTEAL_[A-Z]\b': 'TEAL',
        # Gray variants
        r'\bGRAY_[A-Z]\b': 'GRAY',
    }
    
    for pattern, replacement in color_replacements.items():
        code = re.sub(pattern, replacement, code)
    
    return code


def post_process_code(code: str) -> str:
    """
    Main entry point for code post-processing.
    
    Applies all fixes to AI-generated Manim code.
    
    Args:
        code: Raw generated code
    
    Returns:
        Cleaned and fixed code
    """
    # Check if we need to add header (before making changes)
    has_undefined_colors = bool(re.search(r'\b(ORANGE|RED|BLUE|GREEN|YELLOW|PURPLE|PINK|TEAL|GRAY)_[A-Z]\b', code))
    
    # Apply fixes
    code = fix_undefined_colors(code)
    code = fix_surrounding_rectangles(code)
    
    # Add header comment explaining post-processing
    header = """# NOTE: This code has been automatically post-processed to fix common issues.
# Indexed SurroundingRectangle calls have been disabled as they don't reliably
# highlight the intended equation parts in MathTex objects.
# Undefined color constants have been replaced with standard Manim colors.

"""
    
    # Only add header if we actually made changes
    if '# Auto-disabled:' in code or has_undefined_colors:
        code = header + code
    
    return code


def validate_code_structure(code: str) -> List[str]:
    """
    Validate the generated code for common issues.
    
    Returns:
        List of warning messages (empty if no issues)
    """
    warnings = []
    
    # Check for common issues
    if 'SurroundingRectangle(' in code:
        if re.search(r'SurroundingRectangle\([^,\)]*\[\d+\]', code):
            warnings.append("Code contains indexed SurroundingRectangle calls (will be auto-fixed)")
    
    if 'from manim_voiceover.services.gtts import GTTSService' in code:
        warnings.append("Code still uses deprecated GTTSService (should use ElevenLabsService)")
    
    return warnings
