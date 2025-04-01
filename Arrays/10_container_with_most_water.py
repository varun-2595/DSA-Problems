"""
Problem Statement:
Given n non-negative integers a1, a2, ..., an where each represents a point at coordinate (i, ai), n vertical lines are drawn such that 
the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that 
the container contains the most water.
Notice that you may not slant the container.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) 
the container can contain is 49.

Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""

from typing import List

def maxArea(height: List[int]) -> int:
    checker = 0
    for i in height:
        for j in range(height.index(i)+1, len(height)):
            min_h = min(i, height[j])
            width = j - height.index(i)
            checker = max(checker, (min_h*width))

    return checker



# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))  # Output: 49
height = [1, 1]
print(maxArea(height))  # Output: 1
height = [1, 2, 3, 4, 5]
print(maxArea(height))  # Output: 6