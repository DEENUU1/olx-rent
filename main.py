import os

from dotenv import load_dotenv

from google_sheet import GoogleSheet
from olx import OLX

load_dotenv()

OLX_URL = os.getenv("OLX_URL")
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")


def main() -> None:
    olx = OLX()
    offers = olx.scrape(OLX_URL, 3)

    for offer in offers:
        google_sheet = GoogleSheet(GOOGLE_SHEET_URL)

        if google_sheet.data_exists(2, offer.url):
            continue

        google_sheet.add_data(data=offer)

    return


if __name__ == "__main__":
    main()
