'''
https://leetcode.com/problems/contiguous-array/
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp  = {0:-1}
        pre = 0
        rst = 0
        for i, v in enumerate(nums):
            pre = pre + 1 if v == 1 else pre - 1
            if pre in mp:
                rst = max(rst, i - mp[pre])
            else:
                mp[pre] = i
        return rst