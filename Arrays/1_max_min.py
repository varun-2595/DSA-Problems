"""
1.1 Find the Maximum and Minimum Element in an Array
Problem Statement:
Given an array nums of size n, return the minimum and maximum elements.

Function Signature:
def findMinMax(nums: List[int]) -> Tuple[int, int]:

Example 1:
Input: nums = [3, 1, 5, 7, 9, 2]
Output: (1, 9)

Example 2:
Input: nums = [10, 15, 20, 25]
Output: (10, 25)

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List, Tuple


def findMinMax(nums: List[int]) -> Tuple[int, int]:
    """
    Find the minimum and maximum elements in the array.

    :param nums: List of integers
    :return: Tuple containing the minimum and maximum elements
    """
    max_num = max(nums)
    min_num = min(nums)

    return (min_num, max_num)


# nums = [10, 15, 20, 25]
# print(findMinMax(nums))