def kadane(nums):
    current_max = global_max = nums[0]
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        global_max = max(global_max, current_max)
    return global_max

# Versión circular (para arreglos circulares)
def circular_kadane(nums):
    total = sum(nums)
    min_sum = max_sum = current_min = current_max = nums[0]
    
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)
    
    return max(max_sum, total - min_sum) if max_sum > 0 else max_sum

# Ejemplo: Maximum Sum Circular Subarray (LeetCode 918)