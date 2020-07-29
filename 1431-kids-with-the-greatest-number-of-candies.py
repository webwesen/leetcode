# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        res = list() 
        curr_max = max(candies)
        
        for i in candies:
            res.append((i + extraCandies) >= curr_max)
        
        return res
