'''
https://leetcode.com/problems/combination-sum-iv/
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        rst , tmp = [], []
        n = len(nums)
        mp = {}
        def f(rst , tmp, target, mp):
            if target in mp:
                return mp[target]
            cnt = 0 
            if target == 0:
                mp[target] = 1
                return 1 
            for i in range(n):
                if nums[i] <= target:
                    # tmp.append(nums[i])
                    cnt += f(rst, tmp, target - nums[i], mp)
                    # tmp.pop()
            mp[target] = cnt
            return cnt
            
            
        ans = f(rst , tmp, target, mp)
        return ans