def four_pointers(arr1, arr2, arr3, arr4):
    sum_map = {}
    # Calcular todas las sumas posibles entre arr1 y arr2
    for a in arr1:
        for b in arr2:
            total = a + b
            sum_map[total] = sum_map.get(total, 0) + 1
    
    count = 0
    # Buscar sumas complementarias en arr3 y arr4
    for c in arr3:
        for d in arr4:
            complement = - (c + d)
            if complement in sum_map:
                count += sum_map[complement]
    
    return count

# Ejemplo: 4Sum II (LeetCode 454)