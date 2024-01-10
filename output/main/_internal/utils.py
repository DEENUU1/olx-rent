import logging


def get_urls_from_file():
    try:
        with open('urls.txt', 'r') as f:
            urls = f.readlines()
            return urls
    except Exception as e:
        logging.info(e)
