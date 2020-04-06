'''
https://leetcode.com/problems/maximum-subarray/
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        rst = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max( nums[i], nums[i] + dp[i-1] )
            rst = max(rst, dp[i])
        return rst