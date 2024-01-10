import logging
import pandas as pd


def get_urls_from_file():
    try:
        with open('urls.txt', 'r') as f:
            urls = f.readlines()
            return urls
    except Exception as e:
        logging.info(e)


def get_dataframe_from_file(file: str) -> pd.DataFrame | None:
    """ Return dataframe from file """
    try:
        df = pd.read_excel(file)
        return df
    except Exception as e:
        logging.error(e)
        return None
