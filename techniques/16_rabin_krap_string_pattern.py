def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0: return 0
    if n < m: return -1
    
    # Constantes para hashing
    base = 256
    mod = 10**9 + 7
    base_m = pow(base, m - 1, mod)
    
    # Calcular hash del patrón y primera ventana
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod
    
    # Deslizar ventana
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i+m] == pattern:
                return i
        
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * base_m) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod
            window_hash = (window_hash + mod) % mod  # Evitar negativo
    
    return -1

# Ejemplo: Implement strStr() (LeetCode 28)