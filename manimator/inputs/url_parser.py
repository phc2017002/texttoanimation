import logging
import requests
from bs4 import BeautifulSoup
from readability import Document

logger = logging.getLogger(__name__)

class URLParser:
    """
    Extracts main content from URLs.
    """
    
    @staticmethod
    def parse(url: str) -> str:
        """
        Extract main text content from a URL.
        """
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        logger.info(f"Fetching URL: {url}")
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Use readability to extract the main article content
            doc = Document(response.text)
            summary_html = doc.summary()
            title = doc.title()
            
            # Clean up HTML to get plain text
            soup = BeautifulSoup(summary_html, 'html.parser')
            text = soup.get_text(separator='\n\n')
            
            # Clean up whitespace
            clean_text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
            
            full_content = f"Title: {title}\n\n{clean_text}"
            logger.info(f"Extracted {len(full_content)} characters from URL")
            
            return full_content
            
        except Exception as e:
            logger.error(f"Error parsing URL: {e}")
            raise RuntimeError(f"Failed to parse URL: {e}")
