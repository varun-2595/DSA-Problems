"""
1.2 Reverse an Array In-Place
Problem Statement:
Given an array nums, reverse the array in-place without using extra space.

Function Signature:
def reverseArray(nums: List[int]) -> None:

Example 1:
Input: nums = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Example 2:
Input: nums = [10, 20, 30]
Output: [30, 20, 10]

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List

def reverseArray(nums: List[int]) -> None:
    new_list = []
    for i in range(len(nums)):
        new_list.append(nums[len(nums) - 1 - i])

    return new_list



# Example usage:
# nums = [30, 20, 10]
# print(reverseArray(nums))