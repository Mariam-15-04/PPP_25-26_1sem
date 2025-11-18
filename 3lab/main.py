def find_shortest_path_simple(graph, start, end):

    best_path = None
    best_distance = float('inf')
    
    def dfs(current, path, distance):
        nonlocal best_path, best_distance
        
        current_path = path + [current]
        
        print(f"В вершине {current}, Путь: {' -> '.join(current_path)}, Расстояние: {distance}")
        
        if current == end:
            print(f"Достигнута конечная вершина!")
            if distance < best_distance:
                best_distance = distance
                best_path = current_path.copy()
                print(f"Новый кратчайший путь! Расстояние: {distance}")
            return
        
        for neighbor, weight in graph.get(current, {}).items():
            if neighbor in current_path:
                continue
            print(f"Пробуем: {current} -> {neighbor} (расстояние: {weight})")
            dfs(neighbor, current_path, distance + weight)
    
    print("Начинаем поиск кратчайшего пути")
    print("=" * 40)
    dfs(start, [], 0)
    
    return best_path, best_distance

if __name__ == "__main__":  
    graph = {'A': {'B': 3, 'C': 1}, 'B': {'A': 3, 'D': 2}, 'C': {'A': 1, 'D': 4},
             'D': {'B': 2, 'C': 4, 'E': 1}, 'E': {'D': 1}}
    
    print("граф:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {neighbors}")
    
    print("\n" + "="*50)
    path, distance = find_shortest_path_simple(graph, 'A', 'E')
    
    print("\n" + "="*50)
    print("результат:")
    if path:
        print(f"Кратчайший путь: {' -> '.join(path)}")
        print(f"Расстояние: {distance}")
    else:
        print("Путь не найден")
