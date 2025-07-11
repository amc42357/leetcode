""" 15. 3Sum
https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the input array
        nums = sorted(nums)
        triplets: List[List[int]] = []

        # Step 2: Iterate through the array, skipping duplicates
        for i in range(len(nums) - 2):
            if self.is_duplicate(nums, i):
                continue
            # Step 3: Use two pointers to find pairs that sum to -nums[i]
            self.find_pairs(nums, i, triplets)
        return triplets

    def is_duplicate(self, nums: List[int], i: int) -> bool:
        # Check if current number is a duplicate of the previous
        return i > 0 and nums[i] == nums[i - 1]

    def find_pairs(self, nums: List[int], i: int, triplets: List[List[int]]) -> None:
        left: int = i + 1
        right: int = len(nums) - 1
        while left < right:
            current_sum: int = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left = self.skip_duplicates_left(nums, left, right)
                right = self.skip_duplicates_right(nums, left, right)
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    def skip_duplicates_left(self, nums: List[int], left: int, right: int) -> int:
        # Move left pointer to the next unique number
        while left < right and nums[left] == nums[left + 1]:
            left += 1
        return left + 1

    def skip_duplicates_right(self, nums: List[int], left: int, right: int) -> int:
        # Move right pointer to the previous unique number
        while left < right and nums[right] == nums[right - 1]:
            right -= 1
        return right - 1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
    print(solution.threeSum([0, 1, 1]))              # Output: []
    print(solution.threeSum([0, 0, 0]))              # Output: [[0, 0, 0]]