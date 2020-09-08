# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        ans = 0
        
        myproduct = 1
        mysum = 0
  
        while (n != 0): 
            myproduct = myproduct * (n % 10)
            mysum = mysum + (n % 10)
            n = n // 10
            
        ans = myproduct - mysum
        
        return ans
