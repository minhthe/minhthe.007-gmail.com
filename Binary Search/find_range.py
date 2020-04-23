'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

'''
import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :return  [-1,-1]
        a, b = bisect.bisect_left(nums, target), bisect.bisect_left(nums, target+1) - 1
        
        return [a,b] if a < len(nums) and  nums[a] == target and nums[b] == target else [-1,-1]