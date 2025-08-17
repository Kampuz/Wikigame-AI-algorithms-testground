import requests
import time

API_URL = "https://pt.wikipedia.org/w/api.php"

def get_links(title):
    """Fetch all main-namespace links from a Wikipedia page."""
    params = {
        "action": "query",
        "titles": title,
        "prop": "links",
        "plnamespace": 0,
        "format": "json",
        "pllimit": "max"
    }
    response = requests.get(API_URL, params=params).json()
    pages = response.get("query", {}).get("pages", {})

    links = []
    for page in pages.values():
        for link in page.get("links", []):
            links.append(link["title"])

    time.sleep(0.5)
    return links