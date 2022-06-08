import socket
from urllib.parse import urlparse

from browser_history import get_history


def url_from_history():
    """url_from_history _summary_

    Get the urls from the browser history

    Returns:
        list: A list of urls

    Examples:
        >>> url_from_history()
        ['https://www.google.com/search?channel=fs&client=ubuntu&q=github', 'http://yahoo.com']
    """
    outputs = get_history()  # https://github.com/browser-history/browser-history

    # this is a list of (datetime.datetime, url) tuples
    his = outputs.histories
    urls = []
    for item in his:
        url = item[1]
        urls.append(url)
    return urls


def get_netloc(urls: list) -> list:
    """get_netloc _summary_

    Get the netloc from a list of urls

    Args:
        urls (list): A list of urls

    Returns:
        list: A list of netlocs

    Examples:
        >>> get_netloc(['https://www.google.com/search?channel=fs&client=ubuntu&q=github'', 'http://yahoo.com'])
        ['google.com', 'yahoo.com']
    """
    netlocs = set()
    for url in urls:
        try:
            # https://stackoverflow.com/questions/44113335/extract-domain-from-url-in-python
            netloc = urlparse(url).netloc
            netlocs.add(netloc)
        except Exception as e:
            print(e)
    return netlocs


def get_ip(netlocs: list) -> list:
    """get_hostname _summary_

    Get the hostname from a list of netlocs

    Args:
        netlocs (list): A list of netlocs

    Returns:
        list: A list of hostnames

    Examples:
        >>> get_hostname(['google.com', 'yahoo.com'])
        ['216.58.198.78', '98.137.11.163']
    """
    ip_set = set()
    for netloc in netlocs:
        try:
            # https://stackoverflow.com/a/166520
            hostname = socket.gethostbyname(netloc)
            ip_set.add(hostname)
        except Exception as e:
            print(e)
    return ip_set


# TODO:  IP address to location
