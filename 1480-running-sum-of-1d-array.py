# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = list()        
        for i, v in enumerate(nums):
            res.append(sum(nums[:i+1]))
        
        return res
        
# ===

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = list()
        running_sum = 0
        
        for i in nums:
            running_sum = running_sum + i
            res.append(running_sum)
        
        return res
