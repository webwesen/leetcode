# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ans = list()
        n = len(nums)
        
        for i in range(n):
            counter = 0
            for j in range(n):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    counter += 1
            ans.append(counter)
        
        return ans
        
# ===

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        n = sorted(nums)
        d = dict()
        ans = list()

        for i in range(len(n)):
            if n[i] not in d:
                d[n[i]] = i
        
        for i in nums:
            ans.append(d[i])
            
        return ans
