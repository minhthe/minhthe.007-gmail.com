'''
https://leetcode.com/problems/third-maximum-number
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        tmp = list(set(nums))
        if(len(tmp) <=2): return max(tmp)
        
        k = 3 
        max_val = int(1e9)
        def f(tmp, max_val):
            # find element that greater all and smaller max_val:
            rst = tmp[0]
            for i in range(1, len(tmp)):
                rst = tmp[i] if tmp[i] > rst  and tmp[i] < max_val else rst
            return rst
        for i in range(3):
            max_val = f(tmp, max_val)
        return max_val