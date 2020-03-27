'''

https://leetcode.com/problems/house-robber

This solution cached with 2 variables. Which is because familiar with 2 variables to sovle the rob -iii. just run from 1->n. and if meed condition, continue with.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        u,v, nums, memo = 0,0, nums, {}
        def f(root, pos , nums, memo):
            # print(root, pos)
            if((root,pos) in memo): return memo[(root, pos)]
            if(pos >= len(nums) or root >= len(nums)) : return 0
            if(root +1 == pos): return f(root, root+2, nums, memo)
            
            pick = nums[pos] + f(pos, pos+1, nums, memo)
            not_pick = f(pos+1, pos+1, nums, memo)
            memo[(root, pos)] = max(pick, not_pick)
            return memo[(root, pos)]
        return f(u,v, nums, memo)
