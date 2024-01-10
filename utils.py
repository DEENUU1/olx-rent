import logging
import os
from typing import Tuple

import pandas as pd


def get_urls_from_file():
    try:
        with open('urls.txt', 'r') as f:
            urls = f.readlines()
            return urls
    except Exception as e:
        logging.info(e)


def get_file_names_startswith_olx() -> Tuple:
    """ Return tuple of strings with file names which starts from olx phrase """
    file_names = os.listdir()
    file_names_startswith_olx = tuple(filter(lambda x: x.startswith('olx'), file_names))
    return file_names_startswith_olx


def get_dataframe_from_file(file: str) -> pd.DataFrame | None:
    """ Return dataframe from file """
    try:
        df = pd.read_excel(file)
        return df
    except Exception as e:
        logging.error(e)
        return None
