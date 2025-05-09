import re
from typing import List, Optional
from fake_useragent import UserAgent
import httpx
import re

def fetch_html(url: str, referer:str="") -> str:
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Referer": referer
    }

    try:
        with httpx.Client(headers=headers, timeout=10.0, follow_redirects=True) as client:
            response = client.get(url)
            response.raise_for_status()
            return response.text

    except httpx.HTTPStatusError as e:
        print(f"❌ HTTP error while fetching {url}: {e.response.status_code} - {e}")
    except httpx.RequestError as e:
        print(f"❌ Network error while fetching {url}: {e}")
    except Exception as e:
        print(f"🚨 Unexpected error while fetching {url}: {e}")
    
    return ""



def extract_first_mp4(text: str) -> str:
    """
    Extracts the first MP4 URL from the given text.

    Args:
        text (str): The input text to search for MP4 URLs.

    Returns:
        str: The first MP4 URL if found, otherwise an empty string ("").
    """
    try:
        # Define a regular expression pattern to find MP4 links
        pattern = r"https?://.*?\.mp4"

        # Search for all matches in the input text
        mp4_urls = re.findall(pattern, text)

        # Return the first MP4 URL if available, otherwise return an empty string
        if mp4_urls:
            return mp4_urls[0]
        else:
            return ""

    except Exception as e:
        # Print any unexpected error and return an empty string
        print(f"Error extracting MP4 URL: {str(e)}")
        return ""
