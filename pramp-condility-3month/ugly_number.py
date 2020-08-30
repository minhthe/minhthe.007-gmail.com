'''https://leetcode.com/problems/ugly-number/'''
class Solution:
    def isUgly(self, nums: int) -> bool:
        if nums <=0 : return False
        while  nums % 2==0: nums = nums // 2
        while  nums % 3==0: nums = nums // 3
        while  nums % 5==0: nums = nums // 5    
        return nums == 1