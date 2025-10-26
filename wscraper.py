import requests
from bs4 import BeautifulSoup

def scrape_website(url, scrape_option):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        if scrape_option == "Title":
            return soup.title.string if soup.title else "No title found."

        elif scrape_option == "All Paragraphs":
            paragraphs = [p.get_text() for p in soup.find_all('p')]
            return "\n\n".join(paragraphs) if paragraphs else "No paragraphs found."

        elif scrape_option == "All Links":
            links = [a['href'] for a in soup.find_all('a', href=True)]
            return "\n".join(links) if links else "No links found."

        elif scrape_option == "All Headings (H1-H6)":
            headings = []
            for level in range(1, 7):
                headings.extend([h.get_text() for h in soup.find_all(f'h{level}')])
            return "\n".join(headings) if headings else "No headings found."

        elif scrape_option == "Images":
            images = [img['src'] for img in soup.find_all('img', src=True)]
            return "\n".join(images) if images else "No images found."

        else:
            return "Invalid scrape option selected."

    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the URL: {e}"

