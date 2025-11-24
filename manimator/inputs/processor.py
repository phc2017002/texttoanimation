import logging
from pathlib import Path
from typing import Union
from .pdf_parser import PDFParser
from .url_parser import URLParser

logger = logging.getLogger(__name__)

class InputProcessor:
    """
    Main entry point for processing different types of inputs.
    """
    
    @staticmethod
    def process(input_type: str, input_data: str) -> str:
        """
        Process input based on type.
        
        Args:
            input_type: 'text', 'pdf', or 'url'
            input_data: The actual text, file path, or URL
            
        Returns:
            Extracted text content
        """
        logger.info(f"Processing input type: {input_type}")
        
        if input_type == 'text':
            return input_data
            
        elif input_type == 'pdf':
            return PDFParser.parse(input_data)
            
        elif input_type == 'url':
            return URLParser.parse(input_data)
            
        else:
            raise ValueError(f"Unsupported input type: {input_type}")
