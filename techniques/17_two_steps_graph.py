def two_step_bfs(graph, start):
    # Paso 1: BFS desde inicio para calcular distancias
    dist_start = [-1] * len(graph)
    dist_start[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist_start[neighbor] == -1:
                dist_start[neighbor] = dist_start[node] + 1
                queue.append(neighbor)
    
    # Paso 2: BFS desde objetivo para encontrar caminos
    # (Implementación similar para dist_target)
    
    # Combinar resultados
    min_distance = float('inf')
    for i in range(len(graph)):
        if dist_start[i] != -1 and dist_target[i] != -1:
            min_distance = min(min_distance, dist_start[i] + dist_target[i])
    
    return min_distance

# Ejemplo: Shortest Path in Undirected Graph