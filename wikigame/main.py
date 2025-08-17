from algorithms import *

if __name__ == "__main__":
    start_article = input("Start article: ").capitalize()
    
    target_article = input("Target article: ").capitalize()
    
    search_type = input("Search type (BFS/DFS/DLS/IDS/UCS): ")
    
    max_depth = int(input("Max depth: "))

    if search_type.upper() == "BFS":
        path = bfs.bfs(start_article, target_article, max_depth)
    elif search_type.upper() == "DFS":
        path = dfs(start_article, target_article, max_depth)
    elif search_type.upper() == "DLS":
        path = dls(start_article, target_article, max_depth)
    elif search_type.upper() == "IDS":
        path = ids(start_article, target_article, max_depth)
    elif search_type.upper() == "UCS":
        path = ucs(start_article, target_article, max_depth)
    else:
        print("Opção Inválida.")
