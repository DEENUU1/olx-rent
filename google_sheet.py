import gspread

from offer import Offer
from utils import get_current_date
import time


class GoogleSheet:
    """
    Class for interacting with a Google Sheet.
    """

    def __init__(
            self,
            document_url: str,
            credentials_file_name: str = "credentials.json"
    ) -> None:
        """Initialize GoogleSheet with document URL and credentials filename.

        Args:
            document_url (str): The URL of the Google Sheet document.
            credentials_file_name (str, optional): The filename of the
                credentials file. Defaults to "credentials.json".
        """
        self.document_url = document_url
        self.service_account = gspread.service_account(filename=credentials_file_name)

    def get_sheet(self) -> gspread.Worksheet:
        """Get the Google Sheet worksheet.

        Returns:
            gspread.Worksheet: The Google Sheet worksheet.
        """
        return self.service_account.open_by_url(self.document_url).sheet1

    def data_exists(self, url_column: int, url: str) -> bool:
        """Check if data exists in the Google Sheet.

        Args:
            url_column (int): The index of the column where URLs are stored.
            url (str): The URL to check for existence.

        Returns:
            bool: True if data exists, False otherwise.
        """
        # Rate limit Google Sheet API (60 requests per minute)

        time.sleep(2)
        try:
            cell = self.get_sheet().find(url, in_column=url_column)
            if cell:
                print("Offer exists in google sheet")

                return True
            return False

        except gspread.exceptions.APIError:
            return False

        except Exception as e:
            print(e)
            return False

    def add_data(self, data: Offer) -> None:
        """Add data to the Google Sheet.

        Args:
            data (Offer): The offer data to add.
        """
        # Rate limit Google Sheet API (60 requests per minute)
        time.sleep(2)

        try:
            row_data = [
                data.title,
                data.url,
                data.price,
                data.district,
                data.map_url,
                str(get_current_date())
            ]
            self.get_sheet().insert_row(row_data, index=2)
            print("Save data to Google Sheet")

        except gspread.exceptions.APIError as e:
            print(e)
            return

        except Exception as e:
            print(e)
            return
