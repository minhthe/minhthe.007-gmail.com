'''
https://leetcode.com/problems/maximum-subarray/

*** approach:kadane O(n)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        rst = nums[0]
        start = end  = 0
        for i in range(len(nums)):
            s += nums[i]
            if(rst < s):
                rst = s
                end = i
            if s < 0 :
                s = 0
                start = i+1
        print(nums[start:end+1])
        return rst
                