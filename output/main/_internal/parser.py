import logging
from typing import List, Dict, Optional, Tuple, Generator

import pandas

from schemas import Params, Price, Object


def parse_params(params) -> Tuple[List[Optional[Params]], Optional[Price], Optional[Price]]:
    """
    Parse the given params to create a list of Params objects and extract the Price object.

    :param params: A list of dictionaries representing the params.
    :return: A tuple containing the list of Params objects and the Price object.
    """
    params_list = []
    price = None
    rent = None

    for param in params:
        key, label = param["key"], param["value"]["label"]
        if key == "price":
            price = Price(
                value=param.get("value", {}).get("value"),
            )
        if key == "rent":
            rent = Price(
                value=param.get("value", {}).get("key"),
            )

        obj = None
        if key == "price" or key == "rent":
            pass
        elif key == "m":
            m_value = param.get("value", {}).get("key")
            obj = Params(name=key, label=m_value)
        else:
            obj = Params(name=key, label=label)

        if obj:
            params_list.append(obj)

    return params_list, price, rent


def parse_data(data: List[Dict]) -> Generator[Object, None, None]:
    """
    This method `parse_data` takes a list of dictionaries as input and returns a generator object.
    Each dictionary in the input list represents an item, and within that item, there is a nested "data" key which
    contains a list of offers. Each offer is further processed using the `parse_params`
    function to extract parameters and price.

    :return: A generator object that yields instances of the Object class.
    """
    for item in data:
        for offer in item["data"]:
            params, price, rent = parse_params(offer["params"])

            yield Object(
                url=offer["url"],
                title=offer["title"],
                created_time=offer["created_time"],
                city=offer.get("location", {}).get("city", {}).get("name"),
                district=offer.get("location", {}).get("district", {}).get("name"),
                region=offer.get("location", {}).get("region", {}).get("name"),
                price=price,
                rent=rent,
                params=params
            )


def save_to_xlsx(data) -> bool:
    """
    Save parsed data to xlsx file
    """
    try:
        df = pandas.DataFrame(data)
        df.to_excel("olx.xlsx", index=False)
        return True
    except Exception as e:
        logging.error(f"Error saving data to xlsx: {e}")
        return False


def get_monthly_price(price: float = None, rent: float = None) -> float | None:
    if price and rent:
        return float(price) + float(rent)

    if price is None and rent is None:
        return None

    if price and not rent:
        return price

    if rent and not price:
        return rent


def parser(data) -> bool:
    """
    Scrape data from a given URL and save it to an Excel file.

    :return: None
    """
    objects = parse_data(data)

    dicts = []
    for idx, object_ in enumerate(objects):
        params_dict = {}
        for param in object_.params:
            params_dict[param.name] = param.label

        dicts.append(
            {
                "url": object_.url,
                "title": object_.title,
                "created_time": object_.created_time,
                "city": object_.city if object_.city else None,
                "district": object_.district if object_.district else None,
                "region": object_.region if object_.region else None,
                "price_val": object_.price.value if object_.price else None,
                "rent": object_.rent.value if object_.rent else None,
                "monthly": get_monthly_price(
                    object_.price.value,
                    object_.rent.value
                ) if object_.price and object_.rent else None,
                **params_dict,
            }
        )

    save = save_to_xlsx(dicts)
    if save:
        logging.info("Data saved to xlsx file")
        return True
    else:
        return False
