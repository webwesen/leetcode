# 

class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        ans = 0
        
        while num > 0:
            num = self.process(num)
            ans = ans + 1
            
        return ans
    
    def process(self, num):
        if num % 2:
            return num - 1
        else:
            return num / 2
