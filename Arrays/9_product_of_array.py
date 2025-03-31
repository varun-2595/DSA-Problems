"""
Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm without using the division operation and in O(n) time.

Examples:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    new_nums = nums.copy()
    output = []
    multi = 1
    for i in range(len(nums)):
        new_nums.pop(i)
        for j in new_nums:
            multi *= j
        output.append(multi)
        new_nums = nums.copy()
        multi = 1

    return output


# Example usage:
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))  # Output: [0, 0, 9, 0, 0]
nums = [1, 2, 3, 4, 5]
print(productExceptSelf(nums))  # Output: [120, 60, 40, 30, 24]