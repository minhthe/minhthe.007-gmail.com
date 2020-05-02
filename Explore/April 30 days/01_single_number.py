'''
https://leetcode.com/problems/single-number/

-> using xor to implement it without using extra memory.
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for item in nums:
            tmp ^= item
        return tmp