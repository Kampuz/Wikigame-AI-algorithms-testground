from ..wikiQuery import get_links
from ..print import print_exploration, print_summary
from collections import deque

def dfs(start, goal, max_depth):
    stack = deque([[start]])
    visited = set([start])

    while stack:
        path = stack.pop()
        article = path[-1]

        print_exploration(path, goal)

        if article == goal:
            return print_summary(True, path, len(visited))

        if len(path) > max_depth:
            continue

        for neighbor in get_links(article):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(path + [neighbor])
    
    return print_summary(False, [], len(visited))