__author__ = 'github.com/samshadwell'

import wiki_bfs

shortcut_mapping = {}

print(wiki_bfs.wikipedia_bfs("F", "E", shortcut_mapping))
print(wiki_bfs.wikipedia_bfs("A", "E", shortcut_mapping))
print(wiki_bfs.wikipedia_bfs("B", "E", shortcut_mapping))
