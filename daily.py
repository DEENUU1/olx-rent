from get_content import GetOlxContent
from parser import parse_data, get_monthly_price
from utils import get_urls_from_file
from datetime import datetime, timedelta


def is_today(date_str):
    created_datetime = datetime.fromisoformat(date_str)
    current_date = datetime.now().date()
    return created_datetime.date() == current_date


def daily_offer(data):
    objects = parse_data(data)

    for object_ in objects:
        if is_today(object_.created_time):
            yield f"{object_.url} | {object_.created_time} | {get_monthly_price(object_.price.value, object_.rent.value) if object_.price and object_.rent else None}"


if __name__ == "__main__":
    urls = get_urls_from_file()

    for url in urls:
        scraper = GetOlxContent(url)
        data = scraper.fetch_content()

        for result in daily_offer(data):
            print(result)