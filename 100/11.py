""" 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/description/
https://leetcode.com/problems/container-with-most-water/submissions/1693552441/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from typing import List

class Solution:
    def max_area(self, height: List[int]) -> int:
        # Two-pointer approach to find the maximum area of water container.
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the width and height of the container.
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update max_area if current_area is larger.
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line inward.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
# Test cases to validate the solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected output: 49
    print(sol.maxArea([1,1]))  # Expected output: 1
    print(sol.maxArea([4,3,2,1,4]))  # Expected output: 16
    print(sol.maxArea([1,2,1]))  # Expected output: 2