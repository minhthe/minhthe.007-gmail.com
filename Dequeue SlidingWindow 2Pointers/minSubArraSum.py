'''
https://leetcode.com/problems/minimum-size-subarray-sum
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        i, rst = 0, len(nums) + 1
        tmp = 0
        for j in range(len(nums)):
            tmp += nums[j]
            while(tmp >= s):
                rst = min(rst, j - i + 1)
                tmp -= nums[i]
                i+=1
        return rst % (len(nums) + 1)
            