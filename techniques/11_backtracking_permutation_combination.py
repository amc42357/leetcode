def backtrack_permutations(nums):
    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    
    nums.sort()
    res = []
    backtrack([], [False]*len(nums))
    return res

# Ejemplo: Permutations II (LeetCode 47)