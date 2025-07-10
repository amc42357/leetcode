def dp_optimized(nums):
    n = len(nums)
    # Usar solo dos filas en lugar de matriz completa
    dp_prev = [0] * n
    dp_curr = [0] * n
    
    for i in range(1, n):
        for j in range(i, n):
            # Actualizar dp_curr basado en dp_prev
            # Ejemplo: Longest Common Subsequence
            if condition:
                dp_curr[j] = dp_prev[j-1] + 1
            else:
                dp_curr[j] = max(dp_prev[j], dp_curr[j-1])
        dp_prev, dp_curr = dp_curr, [0] * n
    
    return dp_prev[-1]

# Ejemplo: Edit Distance (LeetCode 72)