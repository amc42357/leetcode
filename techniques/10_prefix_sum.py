def prefix_sum(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    
    # Query: suma entre índices [i, j]
    def query(i, j):
        return prefix[j + 1] - prefix[i]
    
    return query

# Ejemplo: Subarray Sum Equals K (LeetCode 560)