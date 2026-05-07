# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         max_profit = 0

#         for i in range(len(prices)-1):
#             highest_sell_price = float('-inf')

#             for j in range(i+1, len(prices)):
#                 highest_sell_price = max(highest_sell_price, prices[j])
#                 current_profit = highest_sell_price - prices[i]

#                 max_profit = max(current_profit, max_profit)

#         return max_profit  
    
    # Time: O(n^2)
    # Approach: brute force; nested for loops
    # Notes: exceeds time limit


#################

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        lowest_buy_price = prices[0]
        for i in range(1, len(prices)):
            current_profit = prices[i] - lowest_buy_price
            max_profit = max(max_profit, current_profit)
            lowest_buy_price = min(lowest_buy_price, prices[i])
        return max_profit
    

    # Time: O(n)
    # Approach: 
    # Notes: better