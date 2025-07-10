from collections import deque

def sliding_window_max(nums, k):
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        # Eliminar elementos fuera de la ventana
        if dq and dq[0] == i - k:
            dq.popleft()
        
        # Mantener deque decreciente
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Agregar máximo a resultado
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Ejemplo: Sliding Window Maximum (LeetCode 239)