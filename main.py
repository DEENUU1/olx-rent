import logging

from get_content import GetOlxContent
from parser import parser
from utils import get_urls_from_file


def main():
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
        parser(data)

    logging.info("Scraping process completed.")


if __name__ == "__main__":
    main()
