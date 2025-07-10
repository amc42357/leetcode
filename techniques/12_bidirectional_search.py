from collections import deque

def bidirectional_bfs(start, target):
    if start == target: return 0
    
    # Inicializar dos colas y dos diccionarios de visitados
    queue_start = deque([start])
    queue_target = deque([target])
    visited_start = {start: 0}
    visited_target = {target: 0}
    
    while queue_start and queue_target:
        # Expandir desde el inicio
        for _ in range(len(queue_start)):
            node = queue_start.popleft()
            for neighbor in get_neighbors(node):
                if neighbor in visited_target:
                    return visited_start[node] + 1 + visited_target[neighbor]
                if neighbor not in visited_start:
                    visited_start[neighbor] = visited_start[node] + 1
                    queue_start.append(neighbor)
        
        # Expandir desde el objetivo
        for _ in range(len(queue_target)):
            node = queue_target.popleft()
            for neighbor in get_neighbors(node):
                if neighbor in visited_start:
                    return visited_target[node] + 1 + visited_start[neighbor]
                if neighbor not in visited_target:
                    visited_target[neighbor] = visited_target[node] + 1
                    queue_target.append(neighbor)
    
    return -1  # Sin conexión

# Ejemplo: Word Ladder (LeetCode 127)