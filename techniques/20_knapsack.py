def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][w] = máximo valor con capacidad w usando primeros i items
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w], 
                    values[i-1] + dp[i-1][w - weights[i-1]]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Versión optimizada en espacio
def knapsack_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        # Iterar hacia atrás para evitar sobrescribir valores necesarios
        for w in range(capacity, weights[i]-1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[capacity]

# Ejemplo: Partition Equal Subset Sum (LeetCode 416)