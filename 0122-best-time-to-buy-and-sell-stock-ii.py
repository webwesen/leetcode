# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        
        for i,v in enumerate(prices):
            if i == 0:
                continue
            if v > prices[i-1]:
                ans = ans + prices[i] - prices[i-1]
        
        return ans
