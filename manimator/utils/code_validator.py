"""
Code Validator - Validates generated Manim code before rendering
"""

import ast
import re
from typing import List, Tuple, Optional


class CodeValidator:
    """Validates Manim code for common issues"""
    
    def validate(self, code: str) -> Tuple[bool, List[str]]:
        """
        Validate code and return validation result.
        
        Args:
            code: Python code to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # 1. Syntax validation
        syntax_valid, syntax_errors = self._validate_syntax(code)
        if not syntax_valid:
            errors.extend(syntax_errors)
            return (False, errors)  # Can't continue if syntax is invalid
        
        # 2. Import validation
        import_errors = self._validate_imports(code)
        errors.extend(import_errors)
        
        # 3. Structure validation
        structure_errors = self._validate_structure(code)
        errors.extend(structure_errors)
        
        # 4. Variable/color validation
        variable_errors = self._validate_variables(code)
        errors.extend(variable_errors)
        
        # 5. Voiceover validation
        voiceover_errors = self._validate_voiceover(code)
        errors.extend(voiceover_errors)
        
        is_valid = len(errors) == 0
        return (is_valid, errors)
    
    def _validate_syntax(self, code: str) -> Tuple[bool, List[str]]:
        """Validate Python syntax"""
        try:
            ast.parse(code)
            return (True, [])
        except SyntaxError as e:
            return (False, [f"Syntax error at line {e.lineno}: {e.msg}"])
        except Exception as e:
            return (False, [f"Parse error: {str(e)}"])
    
    def _validate_imports(self, code: str) -> List[str]:
        """Check for required imports"""
        errors = []
        
        # Check for manim import
        if 'from manim import *' not in code and 'import manim' not in code:
            errors.append("Missing required import: from manim import *")
        
        # Check for VoiceoverScene import (from our custom implementation)
        if 'from manimator.scene.voiceover_scene import VoiceoverScene' not in code:
            errors.append("Missing required import: from manimator.scene.voiceover_scene import VoiceoverScene")
        
        # Check for voiceover service import
        if 'from manimator.services.voiceover import SimpleElevenLabsService' not in code:
            errors.append("Missing required import: from manimator.services.voiceover import SimpleElevenLabsService")
        
        # Check for pathlib import (needed for cache_dir)
        if 'from pathlib import Path' not in code:
            errors.append("Missing required import: from pathlib import Path")
        
        return errors
    
    def _validate_structure(self, code: str) -> List[str]:
        """Validate code structure (class, construct method, etc.)"""
        errors = []
        
        # Check for Scene class
        if 'class' not in code:
            errors.append("No class definition found")
            return errors
        
        # Check for VoiceoverScene inheritance
        if 'VoiceoverScene' not in code:
            errors.append("Scene class must inherit from VoiceoverScene")
        
        # Check for construct method
        if 'def construct(self):' not in code and 'def construct(self):' not in code:
            errors.append("No construct() method found")
        
        return errors
    
    def _validate_variables(self, code: str) -> List[str]:
        """Check for undefined variables and colors"""
        errors = []
        
        # Check for undefined color constants
        undefined_colors = re.findall(r'\b(ORANGE|RED|BLUE|GREEN|YELLOW|PURPLE|PINK|TEAL|GRAY)_[A-Z]\b', code)
        if undefined_colors:
            errors.append(f"Undefined color constants found: {', '.join(set(undefined_colors))}")
        
        return errors
    
    def _validate_voiceover(self, code: str) -> List[str]:
        """Validate voiceover setup"""
        errors = []
        
        # Check for voiceover service setup
        if 'set_speech_service' not in code:
            errors.append("Voiceover service not initialized (missing set_speech_service)")
        
        # Check for SimpleElevenLabsService (the actual service we use)
        if 'SimpleElevenLabsService' not in code:
            errors.append("SimpleElevenLabsService not imported or used")
        
        # Check for voiceover blocks
        if 'with self.voiceover' not in code:
            errors.append("No voiceover blocks found (use 'with self.voiceover(text=...)' for narration)")
        
        return errors
    
    def get_fixable_errors(self, errors: List[str]) -> List[str]:
        """Identify errors that can be auto-fixed"""
        fixable_patterns = [
            'Missing required import',
            'Undefined color constants',
            'Voiceover service not initialized',
        ]
        
        fixable = []
        for error in errors:
            for pattern in fixable_patterns:
                if pattern in error:
                    fixable.append(error)
                    break
        
        return fixable

