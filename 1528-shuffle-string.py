# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        ans = str()
        d = dict()
        
        for i,v in enumerate(indices):
            d[v] = s[i]
            
        for key in sorted(d):
            ans = ans + d[key]
            
        return ans

===

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        ans = str()

        for _,v in sorted(zip(indices, list(s))):
            ans = ans + v
        
        return ans
