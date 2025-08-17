from wikiQuery import get_links
from print import print_exploration, print_summary
from collections import deque
import heapq

# -------------------------
# Generic search function
# -------------------------
def search(start, goal, max_depth, method="BFS"):
    """
    Generic search function for BFS or DFS.
    """
    if method.upper() == "BFS":
        container = deque([[start]])
        pop_func = container.popleft
        append_func = container.append
    elif method.upper() == "DFS":
        container = [[start]]
        pop_func = container.pop
        append_func = container.append
    else:
        raise ValueError("Method must be BFS or DFS.")

    visited = set([start])

    while container:
        path = pop_func()
        article = path[-1]

        print_exploration(path, goal)

        if article == goal:
            return print_summary(True, path, len(visited))

        if len(path) > max_depth:
            continue

        for neighbor in get_links(article):
            if neighbor not in visited:
                visited.add(neighbor)
                append_func(path + [neighbor])

    return print_summary(False, [], len(visited))

# -------------------------
# Depth-Limited Search
# -------------------------
def dls(start, goal, limit):
    return search(start, goal, max_depth=limit, method="DFS")

# -------------------------
# Iterative Deepening Search
# -------------------------
def ids(start, goal, max_depth):
    for depth in range(1, max_depth + 1):
        print(f"\n- IDS iteration with depth limit: {depth}")
        path = search(start, goal, max_depth=depth, method="DFS")
        if path:
            return path
    return None

# -------------------------
# Uniform Cost Search
# -------------------------
def ucs(start, goal, max_depth=float('inf')):
    heap = [(0, [start])]  # (cost, path)
    visited = set([start])

    while heap:
        cost, path = heapq.heappop(heap)
        article = path[-1]

        print_exploration(path, goal)

        if article == goal:
            return print_summary(True, path, len(visited))

        if len(path) > max_depth:
            continue

        for neighbor in get_links(article):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(heap, (cost + 1, path + [neighbor]))

    return print_summary(False, [], len(visited))