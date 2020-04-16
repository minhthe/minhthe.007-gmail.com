'''
https://leetcode.com/problems/product-of-array-except-self
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(nums.count(0)>=2):
            return [0 for x in nums]
        if(nums.count(0) == 1):
            rst = 1 
            
            for item in nums:
                if item!=0: rst*= item
            
            tmp = [0 for item in nums]
            tmp[nums.index(0)] = rst
            return tmp
        rst = 1
        for item in nums:
            rst*= item
        return [int(rst/x) for x in nums]