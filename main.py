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


