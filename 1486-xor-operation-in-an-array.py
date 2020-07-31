# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = 0
        i = 0
        l = list()
        
        while i < n:
            l.append(start + 2*i)
            i += 1
        
        for i in l:
            ans = ans ^ i
        
        return ans

# ===

class Solution(object):
    def xorOperation(self, n, start):

        ans = 0
        
        num = [start + 2 * i for i in range(n)]
        for i in num:
            ans = ans ^ i
            
        return ans
