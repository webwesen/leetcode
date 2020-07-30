# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n < 2:
            return 0
        
        min_p = prices[0]
        max_p = 0
        
        for i in prices:
            min_p = min(min_p, i)
            max_p = max(max_p, i - min_p)

        return max_p
