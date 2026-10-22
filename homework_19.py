import csv

import requests
from bs4 import BeautifulSoup


URL = "https://quotes.toscrape.com/tag/life/"
HEADERS = {"User-Agent": "hillel-homework/1.0 (practice)"}


def main():
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    quotes = []

    for quote in soup.select("div.quote"):
        author = quote.select_one("small.author").get_text(strip=True)
        text = quote.select_one("span.text").get_text(strip=True).strip("“”")
        quotes.append({"author": author, "text": text})

    with open("life.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=["author", "text"])
        writer.writeheader()
        writer.writerows(quotes)

    print(f"Збережено {len(quotes)} цитат у life.csv")


if __name__ == "__main__":
    main()