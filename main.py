from mpl_toolkits.basemap import Basemap
import asyncio
import socket
from urllib.parse import urlparse

import ipinfo  # https://github.com/ipinfo/python
from browser_history import get_history

from .const import *

import matplotlib.pyplot as plt
from matplotlib import animation
import mpl_toolkits

mpl_toolkits.__path__.append(MPL_PATH)


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


async def do_req():
    handler = ipinfo.AsyncHandler(
        ACCESS_TOKEN, cache_options={"ttl": 30, "maxsize": 128}
    )
    details = handler.getDetails(IP_ADDRESS)
    cd = list()

    details = await handler.getDetails(ip_address)
    cd.append(details.all)

    return cd


loop = asyncio.get_event_loop()
complete_details = loop.run_until_complete(do_req())

# get IP address to location with ipinfo.io
# get all their including location (lat, lon)
lat = []
lon = []

for loc in complete_details:
    lat.append(float(loc.result()["latitude"]))
    lon.append(float(loc.result()["longitude"]))


# Basic map plot
fig, ax = plt.subplots(figsize=(40, 20))
map = Basemap()

# dark grey land, black lakes
map.fillcontinents(color="#2d2d2d", lake_color="#000000")

# black background
map.drawmapboundary(fill_color="#000000")

# thin white line for country borders
map.drawcountries(linewidth=0.15, color="w")

map.drawstates(linewidth=0.1, color="w")

map.plot(
    lon,
    lat,
    linestyle="none",
    marker="o",
    markersize=25,
    alpha=0.4,
    c="white",
    markeredgecolor="silver",
    markeredgewidth=1,
)


def update_plot(frame_number):
    # update the map
    map.plot(
        lon[frame_number],
        lat[frame_number],
        linestyle="none",
        marker="o",
        markersize=25,
        alpha=0.4,
        c="white",
        markeredgecolor="silver",
        markeredgewidth=1,
    )


def init():
    plt.text(
        -170,
        -72,
        "Server locations of top 500 websites "
        "(by traffic)\nPlot realized with Python and the Basemap library"
        "\n\n~Yusuf\n yusufadell.dev@gmail.com",
        ha="left",
        va="bottom",
        size=28,
        color="silver",
    )


ani = animation.FuncAnimation(fig, update_plot, interval=1, frames=490, init_func=init)


writer = animation.writers["ffmpeg"]
writer = writer(fps=20, metadata=dict(artist="Yusufadel"), bitrate=1800)
ani.save("anim.mp4", writer=writer)
