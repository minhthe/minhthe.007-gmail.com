'''
https://leetcode.com/problems/third-maximum-number
'''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = int(1e10)
        one = - m 
        two = -m
        three = -m
        # nums = list(set(nums))
        # if(len(nums) <= 2): return max(nums)
        for i in range(len(((nums)))):
            if(nums[i] == one or nums[i]==two):
                continue
            if(nums[i]>one):
                three = two
                two = one
                one = nums[i]
            elif(nums[i]>two ):
                three = two
                two = nums[i]
            elif nums[i] > three:
                three = nums[i]
        return three if three != -m else max(nums)
                