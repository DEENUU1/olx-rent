import logging
from datetime import datetime
from typing import List


def get_urls_from_file():
    try:
        with open('urls.txt', 'r') as f:
            urls = f.readlines()
            return urls
    except Exception as e:
        logging.info(e)


def is_today(date_str):
    created_datetime = datetime.fromisoformat(date_str)
    current_date = datetime.now().date()
    return created_datetime.date() == current_date


def get_today_filename():
    date = datetime.now().date()
    return f"{date}.txt"


def item_saved(item: str, filename) -> bool:
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == item:
                return True
    return False


def append_to_file(data: List[str], filename: str) -> None:
    with open(filename, "a") as file:
        for item in data:
            if not item_saved(item, filename):
                file.write(item + "\n")



