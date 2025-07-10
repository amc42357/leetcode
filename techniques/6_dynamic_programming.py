# DP 1D (Fibonacci style)
def dp_1d(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # Casos base
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Relación de recurrencia
    
    return dp[n]

# DP 2D (Tabulation)
def dp_2d(m, n):
    dp = [[0] * n for _ in range(m)]
    
    # Inicializar primera fila/columna
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    # Llenar tabla
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Ejemplo: Unique Paths (LeetCode 62)