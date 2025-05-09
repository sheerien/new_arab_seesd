# from src.etl import (
#     fetch_html,
#     fetch_episode_links,
#     fetch_watch_link,
#     extract_first_mp4,
#     fetch_iframe_src,
#     fetch_mp4_from_watch_link
# )
# from selectolax.parser import HTMLParser
# from src.selectors import selectors

# url = r"https://m15.asd.rest/%d9%85%d8%b3%d9%84%d8%b3%d9%84-%d8%a7%d9%84%d8%ba%d8%b2%d8%a7%d9%84-%d8%a7%d9%84%d9%85%d9%88%d8%b3%d9%85-%d8%a7%d9%84%d8%a7%d9%88%d9%84-%d8%a7%d9%84%d8%ad%d9%84%d9%82%d8%a9-4-%d8%a7%d9%84%d8%b1%d8%a7/"
# print()
# print("Welcome to the MP4 Fetcher!")
# print("This script will help you fetch MP4 links from a given URL.")
# print()
# url = input("Enter the URL: ")
# print()
# eps = fetch_episode_links(url)

# mp4s = []
# for i, ep in enumerate(eps):
#     print()
#     print(f"{i+1} - {ep}")
#     print()
#     print("Fetching watch link...")
#     print()
#     watch_link = fetch_watch_link(ep)
#     print(watch_link)
#     print()
#     mp4 = fetch_mp4_from_watch_link(watch_link)
#     print(mp4)
#     mp4s.append(mp4)


# for mp4 in mp4s:
#     print(f'"{mp4}",')

from src.etl import (
    fetch_html,
    fetch_episode_links,
    fetch_watch_link,
    extract_first_mp4,
    fetch_iframe_src,
    fetch_mp4_from_watch_link
)
from selectolax.parser import HTMLParser
from src.selectors import selectors

def main() -> None:
    """
    Main function to fetch MP4 links from a provided URL.
    
    Prompts the user for a series URL, extracts episode links,
    fetches the watch link for each episode, and extracts the MP4 URL.
    """
    print("\nWelcome to the MP4 Fetcher!")
    print("This script will help you fetch MP4 links from a given URL.\n")

    # Prompt the user to enter the URL
    url = input("Enter the URL: ").strip()
    print()

    # Fetch all episode links
    episodes = fetch_episode_links(url)

    # Initialize list to store extracted MP4 links
    mp4_links = []

    # Loop through each episode link
    for i, ep in enumerate(episodes):
        print()
        print(f"Processing Episode {i+1}: {ep}\n")
        
        try:
            print("Fetching watch link...")
            print()
            watch_link = fetch_watch_link(ep)
            print(f"Watch Link: {watch_link}\n")
            print()
            
            print("Fetching MP4 link...")
            print()
            mp4 = fetch_mp4_from_watch_link(watch_link)
            print(f"MP4 Link: {mp4}\n")
            
            mp4_links.append(mp4)
        
        except Exception as e:
            # Handle any unexpected error per episode to continue processing the rest
            print(f"Error processing episode {i+1}: {e}")
            mp4_links.append("")  # Add empty string if error occurred

    # Print all collected MP4 links
    print("\nAll MP4 Links:")
    print()
    for mp4 in mp4_links:
        print()
        print(f'"{mp4}",')

if __name__ == "__main__":
    main()
