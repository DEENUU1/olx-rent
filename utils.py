

def get_urls_from_file():
    with open('urls.txt', 'r') as f:
        urls = f.readlines()
        return urls
