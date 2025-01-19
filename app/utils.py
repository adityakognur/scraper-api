# app/utils.py
from typing import Optional
from bs4 import BeautifulSoup

def get_css_selector(html: str) -> Optional[str]:
    # In this example, the selector might look for review containers
    soup = BeautifulSoup(html, 'html.parser')
    review_section = soup.find_all('div', {'data-asin': True})  # Example
    if review_section:
        return 'div[data-asin]'  # Adjust as per actual site structure
    return None
