"""
Problem Statement:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Examples:
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    max_count = 0
    unique_list = list(set(nums))
    for i in unique_list:
        count = 0
        for j in nums:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count
            majority = i
    return majority


# Example usage:
nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3
nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  # Output: 2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(majorityElement(nums))  # Output: 1
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(majorityElement(nums))  # Output: 1