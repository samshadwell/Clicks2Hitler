__author__ = 'github.com/samshadwell'

import urllib.request
import re

def get_links(url_in, regex):
    """
    Get all the links to wikipedia pages at the given url
    :param url_in: url to get links from
    :return: set of links in arbitrary order
    """

    resp = urllib.request.urlopen(url_in)
    html = str(resp.read())

    links_set = set([])

    for link in regex.findall(html):
        links_set.add("http://en.wikipedia.org" + link.split("\"")[1])

    return links_set


regex = re.compile('(?:a href=("\/wiki\/[^:]*?"))')



