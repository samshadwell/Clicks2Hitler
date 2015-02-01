__author__ = 'github.com/samshadwell'

import wiki_bfs

shortcut_mapping = {}

num_queries = int(input("How many queries do you want to make? "))

for dummy in range(num_queries):
    in_url = input("Input Wikipedia URL: ")
    print(wiki_bfs.wikipedia_bfs(in_url, "http://en.wikipedia.org/wiki/Adolf_Hitler", shortcut_mapping))
