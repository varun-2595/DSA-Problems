"""
1.3 Find the Second Largest Element
Problem Statement:
Given an array nums, return the second largest element. If there’s no second largest, return -1.

Function Signature:
def secondLargest(nums: List[int]) -> int:

Example 1:
Input: nums = [10, 5, 20, 8, 25]
Output: 20

Example 2:
Input: nums = [4, 4, 4]
Output: -1

Constraints:
2 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List

def secondLargest(nums: List[int]) -> int:
    max_num = max(nums)
    min_num = min(nums)
    second_max = 0
    if max_num == min_num:
        return -1
    nums.remove(max_num)
    second_max = max(nums)
    if second_max == max_num:
        new_nums = [i for i in nums if i != second_max]
    second_max = max(new_nums)

    return second_max


# Example usage:
nums = [25, 5, 25, 25, 25]
print(secondLargest(nums))  # Output: 20
