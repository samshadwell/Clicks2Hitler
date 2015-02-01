__author__ = 'github.com/samshadwell'
import get_wiki_links
import queue
import re

regex = re.compile('(?:a href=("\/wiki\/[^:]*?"))')


def wikipedia_bfs(start_url, end_url, shortcut_mapping):
    """
    Returns the path as an array of urls, where the first corresponds to the start,
    the last corresponds to the end, and the intermediate values are the links from the start to end
    :param start_url: URL to start search from
    :param end_url: URL to end at
    :param shortcut_mapping: mapping "shortcut" that maps from URLs to the URL that is closer to the end
    :return: array of URLs in path from start to end
    """

    shortcut_mapping[end_url] = None

    # Initialize data structures
    q = queue.Queue()
    parents = {}
    dist = 0
    curr_path = []
    path_dist = float("inf")

    parents[start_url] = None
    q.put(start_url)

    # Check to see if the start is the end to save iterations
    if start_url == end_url:
        return [start_url, end_url]

    while not q.empty():

        current = q.get()
        dist += 1

        print("Working with " + current)

        # If we've found a saved path that's better than we can find now, return it
        if dist >= path_dist:
            return curr_path

        # Go through the pages current page links to
        for nbr in get_wiki_links.get_links(current, regex):

            # If we found the end, add this path to the global mapping and return
            if nbr == end_url:
                parents[nbr] = current
                path = path_traceback(parents, nbr)
                add_path_to_mapping(path, shortcut_mapping)
                return path

            # If this nbr is in our global mapping, we should probably see about
            # that shortcut
            elif nbr in shortcut_mapping:
                parents[nbr] = current
                print("Found shortcut for " + nbr + " to end")
                path = path_traceback(parents, nbr)
                ending = path_traceback(shortcut_mapping, nbr)
                ending.reverse()
                ending.remove(nbr)
                curr_path = path + ending
                path_dist = len(curr_path) - 1

            else:
                if nbr not in parents:
                    parents[nbr] = current
                    q.put(nbr)

    return curr_path


def path_traceback(parents, end):
    """
    Return a corresponding to the path from the end specified to the start
    :param parents: mapping of page urls to their "parents" from BFS
    :param end: the URL to start tracing back from
    :return: a list, first entry is the start and the last is the end
    """

    path = [end]
    current = end

    # Trace path back to the source
    while parents[current] is not None:
        path.insert(0, parents[current])
        current = parents[current]

    return path


def add_path_to_mapping(path, shortcut_mapping):
    """
    Add the path to the global mapping, we know the things found are in shortest paths
    :param path: path to add
    :param shortcut_mapping: mapping to add to
    :return: None, adds values to 'shortcut_mapping'
    """

    for idx in range(len(path) - 1):
        shortcut_mapping[path[idx]] = path[idx + 1]