'''
https://leetcode.com/problems/product-of-array-except-self/
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rst = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            rst[i] =rst[i-1]*(nums[i-1])
        tmp = nums[-1]
        for i in range( len(nums) -2, -1, -1 ):
            rst[i] =rst[i]*tmp
            tmp = tmp*nums[i]
        return rst