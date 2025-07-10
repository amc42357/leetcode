def two_pointers(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        # Realizar cálculos con nums[left] y nums[right]
        current = nums[left] + nums[right]
        
        if current == target:
            return [left, right]  # Solución encontrada
        elif current < target:
            left += 1  # Mover puntero izquierdo
        else:
            right -= 1  # Mover puntero derecho
    
    return [-1, -1]  # No encontrado

# Ejemplo: Two Sum II (LeetCode 167)
# Input: nums = [2,7,11,15], target = 9 → Output: [0,1]