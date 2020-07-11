'''
https://leetcode.com/problems/subsets/
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rst, tmp = [],[]
        step = 0 
        def f(rst, tmp, step):
            rst.append(tmp[:])
            
            for i in range(step, len(nums)):
                tmp.append(nums[i])
                f(rst, tmp, i+1)
                tmp.pop()
            return rst
        f(rst, tmp, step)
        return rst