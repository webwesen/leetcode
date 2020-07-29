# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        res = 0
        
        for i,_ in enumerate(nums):
            for j,_ in enumerate(nums):
                if nums[i] == nums[j] and i < j:   
                    res += 1
        
        return res
