import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """Fetches the HTML content of a webpage given a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx errors
        print(f"Successfully fetched {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def parse_page(html):
    """Parses the HTML content and extracts title, paragraphs, and links."""
    soup = BeautifulSoup(html, 'html.parser')

    # Extract title
    title = soup.find('title').get_text() if soup.find('title') else 'No title found'
    
    # Extract paragraphs
    paragraphs = soup.find_all('p')
    paragraph_texts = [p.get_text() for p in paragraphs]

    # Extract links
    links = soup.find_all('a', href=True)
    link_urls = [a['href'] for a in links]

    return title, paragraph_texts, link_urls

def display_data(title, paragraphs, links):
    """Displays the scraped data."""
    print("\n--- Page Title ---")
    print(title)

    print("\n--- Paragraphs ---")
    for i, para in enumerate(paragraphs, 1):
        print(f"{i}. {para}")

    print("\n--- Links ---")
    for i, link in enumerate(links, 1):
        print(f"{i}. {link}")

def main():
    url = input("Enter the URL to scrape: ")
    html_content = fetch_page(url)
    
    if html_content:
        title, paragraphs, links = parse_page(html_content)
        display_data(title, paragraphs, links)

if __name__ == "__main__":
    main()
