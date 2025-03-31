"""
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = min(prices)
    max_price = 0
    if min_price == max_price:
        return 0
    profit = 0
    min_index = prices.index(min_price)
    for i in range(min_index, len(prices)):
        if prices[i] > min_price:
            max_price = max(max_price, prices[i])
    
    profit = max(max_price - min_price, profit)
    return profit


# Example usage:
prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 5