import logging
from pathlib import Path
from typing import Optional
import PyPDF2

logger = logging.getLogger(__name__)

class PDFParser:
    """
    Extracts text from PDF files.
    """
    
    @staticmethod
    def parse(file_path: str | Path) -> str:
        """
        Extract text from a PDF file.
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"PDF file not found: {path}")
            
        logger.info(f"Parsing PDF: {path}")
        
        text_content = []
        
        try:
            with open(path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)
                logger.info(f"PDF has {num_pages} pages")
                
                for i, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text:
                        text_content.append(text)
                        
            full_text = "\n\n".join(text_content)
            logger.info(f"Extracted {len(full_text)} characters from PDF")
            return full_text
            
        except Exception as e:
            logger.error(f"Error parsing PDF: {e}")
            raise RuntimeError(f"Failed to parse PDF: {e}")
