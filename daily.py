from get_content import GetOlxContent
from parser import parse_data, get_monthly_price
from utils import get_urls_from_file, is_today, get_today_filename, append_to_file
from typing import List


def daily_offer(data) -> List:
    res = []

    objects = parse_data(data)

    for object_ in objects:
        if is_today(object_.created_time):
            text = f"{object_.url} | {object_.created_time} | {get_monthly_price(object_.price.value, object_.rent.value) if object_.price and object_.rent else None}"
            res.append(text)

    return res


if __name__ == "__main__":
    urls = get_urls_from_file()

    for url in urls:
        scraper = GetOlxContent(url)
        data = scraper.fetch_content()

        filename = get_today_filename()
        daily = daily_offer(data)
        append_to_file(data=daily, filename=filename)

