# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        
        for i in J:
            ans = ans + S.count(i)
        
        return ans

    
# ===

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([1 for i in S if i in J])
