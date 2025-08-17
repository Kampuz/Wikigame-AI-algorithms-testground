import algoritmos as algo

if __name__ == "__main__":
    start_article = input("Start article: ").capitalize()
    
    target_article = input("Target article: ").capitalize()
    
    search_type = input("Search type (BFS/DFS/DLS/IDS/UCS): ")
    
    max_depth = int(input("Max depth: "))

    if search_type.upper() == "BFS":
        path = algo.bfs(start_article, target_article, max_depth)
    elif search_type.upper() == "DFS":
        path = algo.dfs(start_article, target_article, max_depth)
    elif search_type.upper() == "DLS":
        path = algo.dls(start_article, target_article, max_depth)
    elif search_type.upper() == "IDS":
        path = algo.ids(start_article, target_article, max_depth)
    elif search_type.upper() == "UCS":
        path = algo.ucs(start_article, target_article, max_depth)
    else:
        print("Opção Inválida.")
