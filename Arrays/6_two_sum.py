"""
Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""

from typing import List, Tuple

def twoSum(nums: List[int], target: int) -> Tuple[int, int]:
    output = []
    for i in range(len(nums)):
        if i != len(nums)-1 and (nums[i]) + (nums[i+1]) == target:
            output.append(i)
            output.append(i+1)
            break

    return output


# Example usage:
nums = [3, 7, 2, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]