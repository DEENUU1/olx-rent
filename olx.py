from datetime import datetime
from typing import Optional, List

import requests
from dateutil.parser import parse

from offer import Offer


class OLX:
    """
    A class implementing the scraping strategy for OLX website.
    """

    @staticmethod
    def check_date(created_time: str, max_offer_duration_days: int) -> bool:
        parsed_created_time = parse(created_time)
        today = datetime.now(parsed_created_time.tzinfo)
        different = today - parsed_created_time

        result = different.days <= max_offer_duration_days
        return result

    @staticmethod
    def get_next_page_url(data) -> Optional[str]:
        next_page_element = data.get("links").get("next")

        if not next_page_element:
            return None

        return next_page_element.get("href")

    def scrape(self, url: str, max_offer_duration_days: Optional[int] = None) -> List[Optional[Offer]]:
        """
        Scrape job offers from OLX website.

        Args:
            url (str): The base URL to start scraping from.
            max_offer_duration_days
        Returns:
            List[Optional[Offer]]: A list of scraped offer inputs.
        """

        base_url = url
        offers = []

        while True:
            print(f"Scraping {base_url}")
            response = requests.get(base_url)
            data = response.json()

            if not data:
                break

            for d in data["data"]:
                title = d.get("title")
                offer_url = d.get("url")
                lat = d.get("map", {}).get("lat")
                lon = d.get("map", {}).get("lon")
                location = d.get("location", {})
                district = location.get("district", {}).get("name")
                params = d.get("params")
                price = None
                for param in params:
                    if param.get("key") == "price":
                        price = param.get("value").get("label")

                map_url = None
                if lat and lon:
                    map_url = f"https://www.google.com/maps/@{lat},{lon},20.53z?entry=ttu"

                if not title or not offer_url:
                    continue

                if max_offer_duration_days and not self.check_date(d.get("created_time"), max_offer_duration_days):
                    continue

                offers.append(Offer(title=title, url=offer_url, map_url=map_url, district=district, price=price))

            next_page_url = self.get_next_page_url(data)
            if not next_page_url:
                break

            base_url = next_page_url

        print(f"Scraped {len(offers)} offers")
        return offers