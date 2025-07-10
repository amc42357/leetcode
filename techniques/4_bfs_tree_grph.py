from collections import deque

def bfs(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Ejemplo: Binary Tree Level Order Traversal (LeetCode 102)