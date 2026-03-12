# Distributed Web Crawler & Search Engine (Simplified Version)
# This program crawls web pages, extracts text, builds an index,
# and allows users to search for keywords across crawled pages.
# It demonstrates core ideas behind search engines such as
# crawling, indexing, and query processing.
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# Index structure: word -> list of URLs
search_index = defaultdict(set)

visited_urls = set()


def crawl(url, depth=1):
    """
    Crawls a webpage, extracts words, and stores them in index
    """

    if depth == 0 or url in visited_urls:
        return

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text().lower()
        words = text.split()

        for word in words:
            search_index[word].add(url)

        visited_urls.add(url)

        print("Crawled:", url)

        # Extract links
        for link in soup.find_all("a", href=True):
            next_url = link["href"]

            if next_url.startswith("http"):
                crawl(next_url, depth - 1)

    except:
        pass


def search(query):
    """
    Search query in index
    """

    words = query.lower().split()

    results = None

    for word in words:
        urls = search_index.get(word, set())

        if results is None:
            results = urls
        else:
            results = results.intersection(urls)

    return results


def main():

    seed_url = input("Enter seed URL: ")
    depth = int(input("Enter crawl depth: "))

    crawl(seed_url, depth)

    while True:

        query = input("\nSearch keyword (or 'exit'): ")

        if query == "exit":
            break

        results = search(query)

        if results:
            print("\nSearch Results:")
            for url in results:
                print(url)
        else:
            print("No results found.")


main()