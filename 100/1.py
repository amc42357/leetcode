"""  
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] 

"""

from typing import List

# use two pointers technique
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # Input validation
        if not nums or len(nums) < 2:
            return []
        # Create array of (value, original_index) pairs
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # Sort by value
        indexed_nums.sort()
        
        left = 0
        right = len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum([2, 7, 11, 15], 9))   # Output: [0, 1]
    print(solution.two_sum([3, 2, 4], 6))        # Output: [1, 2]
    print(solution.two_sum([3, 3], 6))           # Output: [0, 1]

