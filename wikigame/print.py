def print_exploration(path, target):
    depth = len(path) -1
    indent = "  " *depth
    article = path[-1]

    if article == target:
        print(f"{indent}- Found target: {article}")
    else:
        print(f"{indent}- {article}")

def print_summary(found, path, visited_count):
    print("\n✅ Search complete!")
    print(f"🔍 Explored {visited_count} articles")

    if found:
        print(f"📚 Path length: {len(path) - 1}")
        print("➡️ Path:", " -> ".join(path))
        return path
    else:
        print("❌ Target not found")
        return None