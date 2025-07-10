def count_inversions(nums):
    def merge_sort_count(nums):
        if len(nums) <= 1:
            return nums, 0
            
        mid = len(nums) // 2
        left, inv_left = merge_sort_count(nums[:mid])
        right, inv_right = merge_sort_count(nums[mid:])
        merged, inv_merge = merge_count(left, right)
        
        return merged, inv_left + inv_right + inv_merge
    
    def merge_count(left, right):
        merged = []
        i = j = inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv += len(left) - i  # Contar inversiones
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv
    
    _, count = merge_sort_count(nums)
    return count

# Ejemplo: Count of Smaller Numbers After Self (LeetCode 315)