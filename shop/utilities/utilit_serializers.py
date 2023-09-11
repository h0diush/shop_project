from urllib.parse import urlparse, urlunparse


def getting_link(current_url, new_path):
    parsed_url = urlparse(current_url)
    new_url = urlunparse(parsed_url._replace(path=new_path))
    return new_url
