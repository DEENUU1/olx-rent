import logging
from get_content import GetOlxContent
from parser import parser
from utils import get_urls_from_file
import subprocess


def get_data():
    """
    Executes the scraping process for each URL provided in the `URLS_TO_SCRAPE` dictionary.
    """
    logging.basicConfig(level=logging.INFO)

    logging.info("Starting scraping process...")

    urls = get_urls_from_file()

    for url in urls:
        scraper = GetOlxContent(url)
        data = scraper.fetch_content()
        logging.info("Finished scraping")

        logging.info("Start parsing scraped data")
        parsed_data = parser(data)
        if parsed_data:
            logging.info(f"Successfully parsed data for {url}: {parsed_data}")
        else:
            logging.warning(f"No data found for {url}")

    logging.info("Scraping process completed.")


if __name__ == "__main__":
    while True:
        options = [
            "0. Quit",
            "1. Get new data",
            "2. Browse data"
        ]
        for option in options:
            print(option)

        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            get_data()
        elif choice == "2":
            subprocess.run(["streamlit", "run", "app.py"])
        else:
            print("Invalid choice. Please try again.")
            continue
