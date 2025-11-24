"""
Code Fixer - Auto-fixes common issues in generated code
"""

import re
from typing import List, Tuple
from .code_postprocessor import post_process_code, fix_undefined_colors
from .code_validator import CodeValidator


class CodeFixer:
    """Auto-fixes common code issues"""
    
    def __init__(self):
        self.validator = CodeValidator()
    
    def auto_fix(self, code: str, errors: List[str]) -> str:
        """
        Attempt to auto-fix code based on errors.
        
        Args:
            code: Code to fix
            errors: List of error messages
            
        Returns:
            Fixed code
        """
        fixed_code = code
        
        # Apply existing post-processor fixes
        fixed_code = post_process_code(fixed_code)
        
        # Fix missing imports
        fixed_code = self._fix_missing_imports(fixed_code, errors)
        
        # Fix undefined colors (already in post_process_code, but ensure it's applied)
        fixed_code = fix_undefined_colors(fixed_code)
        
        # Fix voiceover setup
        fixed_code = self._fix_voiceover_setup(fixed_code, errors)
        
        # Fix common syntax issues
        fixed_code = self._fix_syntax_issues(fixed_code)
        
        return fixed_code
    
    def _fix_missing_imports(self, code: str, errors: List[str]) -> str:
        """Add missing imports"""
        imports_to_add = []
        
        if 'Missing required import: from manim import *' in str(errors):
            if 'from manim import *' not in code:
                imports_to_add.append('from manim import *')
        
        if 'Missing required import: from manimator.scene.voiceover_scene import VoiceoverScene' in str(errors):
            if 'from manimator.scene.voiceover_scene import VoiceoverScene' not in code:
                imports_to_add.append('from manimator.scene.voiceover_scene import VoiceoverScene')
        
        if 'Missing required import: from manimator.services.voiceover import SimpleElevenLabsService' in str(errors):
            if 'from manimator.services.voiceover import SimpleElevenLabsService' not in code:
                imports_to_add.append('from manimator.services.voiceover import SimpleElevenLabsService')
        
        if 'Missing required import: from pathlib import Path' in str(errors):
            if 'from pathlib import Path' not in code:
                imports_to_add.append('from pathlib import Path')
        
        if imports_to_add:
            # Find where to insert imports (after existing imports or at the top)
            lines = code.split('\n')
            insert_idx = 0
            
            # Find last import line
            for i, line in enumerate(lines):
                if line.strip().startswith('import ') or line.strip().startswith('from '):
                    insert_idx = i + 1
            
            # Insert new imports
            for imp in imports_to_add:
                if imp not in code:
                    lines.insert(insert_idx, imp)
                    insert_idx += 1
            
            code = '\n'.join(lines)
        
        return code
    
    def _fix_voiceover_setup(self, code: str, errors: List[str]) -> str:
        """Fix voiceover service setup"""
        if 'Voiceover service not initialized' in str(errors):
            # Find construct method
            construct_match = re.search(r'def construct\(self\):\s*\n', code)
            if construct_match:
                construct_pos = construct_match.end()
                
                # Check if setup already exists
                if 'set_speech_service' not in code[construct_pos:construct_pos+500]:
                    # Find first non-empty line after construct
                    lines = code.split('\n')
                    construct_line_idx = None
                    
                    for i, line in enumerate(lines):
                        if 'def construct(self):' in line:
                            construct_line_idx = i
                            break
                    
                    if construct_line_idx is not None:
                        # Find insertion point (after construct, before other code)
                        insert_idx = construct_line_idx + 1
                        while insert_idx < len(lines) and (not lines[insert_idx].strip() or lines[insert_idx].strip().startswith('#')):
                            insert_idx += 1
                        
                        # Get indentation
                        if insert_idx < len(lines):
                            indent = len(lines[insert_idx]) - len(lines[insert_idx].lstrip())
                        else:
                            indent = 8
                        
                        # Insert voiceover setup with SimpleElevenLabsService
                        setup_line = ' ' * indent + 'self.set_speech_service(SimpleElevenLabsService(voice_id="Rachel", cache_dir=Path("media/voiceover/elevenlabs")))'
                        lines.insert(insert_idx, setup_line)
                        code = '\n'.join(lines)
        
        return code
    
    def _fix_syntax_issues(self, code: str) -> str:
        """Fix common syntax issues"""
        # Fix common indentation issues
        # Fix missing colons after if/for/while
        code = re.sub(r'(if|for|while|def|class)\s+[^:]+$', r'\1:', code, flags=re.MULTILINE)
        
        # Fix double colons
        code = re.sub(r'::', ':', code)
        
        return code
    
    def fix_and_validate(self, code: str, max_attempts: int = 3) -> Tuple[str, bool, List[str]]:
        """
        Fix code and validate until valid or max attempts reached.
        
        Args:
            code: Code to fix
            max_attempts: Maximum fix attempts
            
        Returns:
            Tuple of (fixed_code, is_valid, remaining_errors)
        """
        current_code = code
        
        for attempt in range(max_attempts):
            is_valid, errors = self.validator.validate(current_code)
            
            if is_valid:
                return (current_code, True, [])
            
            # Get fixable errors
            fixable_errors = self.validator.get_fixable_errors(errors)
            
            if not fixable_errors:
                # No more fixable errors
                return (current_code, False, errors)
            
            # Attempt to fix
            current_code = self.auto_fix(current_code, fixable_errors)
        
        # Final validation
        is_valid, final_errors = self.validator.validate(current_code)
        return (current_code, is_valid, final_errors)

