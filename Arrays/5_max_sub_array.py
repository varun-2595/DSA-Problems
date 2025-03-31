"""
1.5 Maximum Subarray Sum (Kadane’s Algorithm)
Problem Statement:
Given an integer array nums, find the contiguous subarray with the largest sum.

Function Signature:
def maxSubArray(nums: List[int]) -> int:

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""


from typing import List

def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        max_sum = max(max_sum, current_sum + nums[i])
        current_sum = max(current_sum + nums[i], nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))  # Output: 6