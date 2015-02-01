__author__ = 'github.com/samshadwell'


def get_links(url_in):
    """
    Get all the links to wikipedia pages at the given url
    :param url_in: url to get links from
    :return: list of links in arbitrary order
    """

    if url_in == "A":
        return ["B", "C"]

    elif url_in == "B":
        return ["A"]

    elif url_in == "C":
        return ["D", "E"]

    elif url_in == "D":
        return []

    elif url_in == "F":
        return ["A"]

    else:
        return []

