"""
Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Examples:
CopyInput: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

from typing import List

def trap(height: List[int]) -> int:
    left_max = height[0]
    right_max = 0
    carry = 0
    for i in range(1, len(height)):
        if i+1 < len(height):
            left_max = max(left_max, height[i-1])
            right_max = max(height[i+1:])
            volume = min(left_max, right_max)
            load = max(0, volume-height[i])
            carry += load

    return carry


# Example usage:
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # Output: 6
height = [4, 2, 0, 3, 2, 5]
print(trap(height))  # Output: 9
height = [1, 2, 3, 4, 5]
print(trap(height))  # Output: 0
