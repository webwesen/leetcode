# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        res = list()
        
        for i in range(n):
            res.extend([nums[i],nums[i+n]])
        
        return res
