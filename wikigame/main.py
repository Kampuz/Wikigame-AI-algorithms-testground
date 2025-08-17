from algorithms import *

# -------------------------
# Main program
# -------------------------
if __name__ == "__main__":
    start_article = input("Start article: ").capitalize()
    target_article = input("Target article: ").capitalize()
    print("\nChoose search method: BFS, DFS, DLS, IDS, UCS")
    method = input("Method: ").upper()

    if method in ["BFS", "DFS"]:
        max_depth = int(input("Max depth: "))
        if method == "BFS":
            path = search(start_article, target_article, max_depth, method="BFS")
        else:
            path = search(start_article, target_article, max_depth, method="DFS")

    elif method == "DLS":
        limit = int(input("Depth limit: "))
        path = dls(start_article, target_article, limit)

    elif method == "IDS":
        max_depth = int(input("Max depth for IDS: "))
        path = ids(start_article, target_article, max_depth)

    elif method == "UCS":
        path = ucs(start_article, target_article)

    else:
        print("Invalid method")
        path = None

    if path:
        print(f"\nPath found ({len(path)-1} steps): {' -> '.join(path)}")
    else:
        print("\nTarget article not found within depth limit.")
