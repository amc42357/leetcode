# DFS para árboles
def dfs_tree(node, result):
    if not node:
        return
    
    # Pre-order traversal
    result.append(node.val)
    dfs_tree(node.left, result)
    dfs_tree(node.right, result)

# Backtracking para combinaciones
def backtrack(path, choices, results):
    if base_condition:
        results.append(path[:])
        return
    
    for choice in choices:
        if not is_valid(choice):
            continue
        
        path.append(choice)  # Hacer elección
        backtrack(path, new_choices, results)  # Explorar
        path.pop()  # Deshacer elección

# Ejemplo: Subsets (LeetCode 78)