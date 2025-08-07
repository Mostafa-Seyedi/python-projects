"""
What is Web Scraping?
---------------------
Web scraping is the process of extracting data from websites. 
To do this effectively, we need a basic understanding of how web pages work 
(HTML structure, tags, classes, etc.).

In Python, the most common libraries used for web scraping are:
- `requests` : for sending HTTP/HTTPS requests and receiving responses.
- `BeautifulSoup` : for parsing and extracting data from HTML or XML documents.
- `lxml` : an optional, faster parser for BeautifulSoup.
- `selenium` : useful for scraping content that requires interaction (e.g., JavaScript rendering, form submission).

In this example, we use `requests` and `BeautifulSoup` to extract the titles of books 
from http://books.toscrape.com/.
"""

import requests
import bs4

# Send a GET request to the target URL
response = requests.get("http://books.toscrape.com/")
response.encoding = 'utf-8'  # Make sure the text is properly encoded

# Check if the request was successful
if response.status_code == 200:
    data = response.text  # Get the HTML content of the page
    soup = bs4.BeautifulSoup(data, 'html.parser')  # Parse HTML

    # Get the page title
    page_title = soup.title.string.strip()
    print(f"\n📄 Page Title: {page_title}\n")

    # Find all book elements
    book_elements = soup.find_all("article", class_='product_pod')
    book_titles = [book.h3.a['title'] for book in book_elements]

    print("📚 Book Titles:")
    for title in book_titles:
        print(f"- {title}")

else:
    print(f"❌ Error connecting to the website. Status code: {response.status_code}")
