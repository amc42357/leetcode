def monotonic_stack(nums):
    stack = []
    result = [0] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result

# Ejemplo: Daily Temperatures (LeetCode 739)