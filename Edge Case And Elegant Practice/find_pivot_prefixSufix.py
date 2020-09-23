'''https://leetcode.com/problems/find-pivot-index/'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        idx = -1
        cur_sum = 0 
        for i,v in enumerate(nums):
            cur_sum += v
            if cur_sum - v == s - cur_sum:
                return i
            
        return idx