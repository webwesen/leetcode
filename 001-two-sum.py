# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = list()
        
        for i in nums:
            compl = target - i
            if compl in nums:
                # edge case : nums = [3,3] target = 6. they expect ans = [0,1]
                if nums.count(i) > 1:
                    ans = [j for j, e in enumerate(nums) if e == i]
                    break
                if compl != i:
                    ans = (nums.index(i), nums.index(compl))
                    break
        
        return ans
