from selectolax.parser import HTMLParser
from .extract import extract_first_mp4, fetch_html
from src.selectors import selectors
from typing import List



def fetch_episode_links(url: str) -> List[str]:
    """
    Fetches and returns a reversed list of episode links from a given URL.
    
    Args:
        url (str): The URL of the page containing the episodes list.
    
    Returns:
        List[str]: A reversed list of episode URLs. Returns an empty list if an error occurs.
    """
    try:
        # Fetch the HTML content from the given URL
        html = fetch_html(url)
        if not html:
            print("Error: Failed to fetch HTML content from the URL.")
            return []

        # Parse the HTML content
        parser = HTMLParser(html)

        # Find the parent element that contains all episode links
        eps_container = parser.css_first(selectors.eps_list)
        if eps_container is None:
            print("Error: Episodes list container not found in the HTML.")
            return []

        # Find all anchor tags within the container
        anchors = eps_container.css("a")
        if not anchors:
            print("Error: No episode links found inside the container.")
            return []

        # Extract the href attributes from the anchor tags
        episodes = [anchor.attributes.get("href").strip() for anchor in anchors if "href" in anchor.attributes]

        # Reverse the list of episodes before returning
        return episodes[::-1]

    except Exception as e:
        # Print the error message and return an empty list
        print(f"Unexpected error occurred: {str(e)}")
        return []




def fetch_iframe_src(watch_link: str) -> str:
    """
    Fetches the iframe 'src' URL from a given watch page link.

    Args:
        watch_link (str): The URL of the watch page.

    Returns:
        str: The iframe 'src' URL if found, otherwise an empty string ("").
    """
    try:
        # Fetch the HTML content of the watch page, using the referer
        html = fetch_html(watch_link, referer=selectors.referer)
        if not html:
            print("Error: Failed to fetch HTML content from the watch link.")
            return ""

        # Parse the HTML content
        parser = HTMLParser(html)

        # Find the iframe element
        iframe = parser.css_first(selectors.iframe)
        if iframe is None:
            print("Error: iframe element not found in the HTML.")
            return ""

        # Extract the 'src' attribute
        src = iframe.attributes.get("src")
        if not src:
            print("Error: 'src' attribute not found in the iframe.")
            return ""

        # Return the cleaned iframe src link
        return src.strip()

    except Exception as e:
        # Print any unexpected error and return an empty string
        print(f"Unexpected error occurred: {str(e)}")
        return ""




def fetch_watch_link(url: str) -> str:
    """
    Fetches the direct watch link from a given episode URL.
    
    Args:
        url (str): The URL of the episode page.
    
    Returns:
        str: The watch link if found, otherwise an empty string ("").
    """
    try:
        # Fetch the HTML content of the episode page
        html = fetch_html(url)
        if not html:
            print("Error: Failed to fetch HTML content from the episode URL.")
            return ""

        # Parse the HTML content
        parser = HTMLParser(html)

        # Find the watch button element
        watch_button = parser.css_first(selectors.watch_buttons)
        if watch_button is None:
            print("Error: Watch button not found in the HTML.")
            return ""

        # Extract the 'href' attribute
        link = watch_button.attributes.get("href")
        if not link:
            print("Error: 'href' attribute not found in the watch button.")
            return ""

        # Return the cleaned link
        return link.strip()

    except Exception as e:
        # Print any unexpected error and return an empty string
        print(f"Unexpected error occurred: {str(e)}")
        return ""




def fetch_mp4_from_watch_link(watch_link: str) -> str:
    """
    Extracts the first MP4 URL from a given watch page link.

    Args:
        watch_link (str): The URL of the watch page.

    Returns:
        str: The first MP4 URL if found, otherwise an empty string ("").
    """
    try:
        # Set the referer to be the base watch link without query parameters
        referer = watch_link.split("?")[0]

        # Fetch the iframe source URL
        iframe = fetch_iframe_src(watch_link)
        if not iframe:
            print("Error: Failed to fetch iframe source.")
            return ""

        # Fetch the HTML content of the iframe
        html = fetch_html(iframe, referer=referer)
        if not html:
            print("Error: Failed to fetch HTML content from iframe.")
            return ""

        # Extract the first MP4 URL from the iframe HTML
        mp4_url = extract_first_mp4(html)
        if not mp4_url:
            print("Error: No MP4 URL found in the iframe HTML.")
            return ""

        # Return the found MP4 URL
        return mp4_url

    except Exception as e:
        # Print any unexpected error and return an empty string
        print(f"Unexpected error occurred: {str(e)}")
        return ""