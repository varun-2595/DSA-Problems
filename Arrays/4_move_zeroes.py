"""
1.4 Move Zeroes to End
Problem Statement:
Given an array nums, move all 0s to the end while maintaining the order of non-zero elements.

Function Signature:
def moveZeroes(nums: List[int]) -> None:

Example 1:
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Example 2:
Input: nums = [0, 0, 0, 1]
Output: [1, 0, 0, 0]

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List

def moveZeroes(nums: List[int]) -> None:
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)

    return nums

# Example usage:
# nums = [0, 1, 0, 3, 12, 0, 11] 
# print(moveZeroes(nums))  # Output: [1, 3, 12, 0, 0]