def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # No encontrado

# Versión avanzada para problemas de optimización:
def min_max_optimization(nums):
    def feasible(guess):
        # Verificar si la solución es factible
        pass
    
    left, right = min_val, max_val
    while left < right:
        mid = (left + right) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Ejemplo: Search in Rotated Sorted Array (LeetCode 33)