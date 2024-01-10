import requests
from typing import Dict, List, Optional
import json
import logging


class GetOlxContent:
    """
    The `GetOlxContent` class is used to fetch content from the OLX website.

    Attributes:
        main_url (str): The main URL of the OLX website.

    Methods:
        fetch_content() -> List[Dict]: Fetches the content from the OLX website and returns it as a list of dictionaries.
        get_next_page_url(json_data) -> Optional[str]: Extracts the URL of the next page from the given JSON data.

    """

    def __init__(self, url: str):
        self.main_url = url
        self.counter = 1

    def fetch_content(self) -> List[Dict]:
        """ Fetch JSON content from url """
        result = []

        while self.main_url:
            logging.info(f"Scraping page {self.counter}...")

            try:
                response = requests.get(self.main_url)
                if response.status_code == 200:
                    json_data = json.loads(response.content)
                    if not json_data:
                        break

                    # Add scraped data to list
                    result.append(json_data)
                    self.main_url = self.get_next_page_url(json_data)
                    self.counter += 1

            except Exception as e:
                logging.error(f"Error fetching content: {e}")

        return result

    @staticmethod
    def get_next_page_url(json_data) -> Optional[str]:
        """ Parse a lint to the next page """
        links = json_data.get("links")
        if links:
            next_page = links.get("next")
            if next_page:
                return next_page.get("href")

        return None
