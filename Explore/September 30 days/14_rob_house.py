class Solution:
    def rob(self, nums: List[int]) -> int:
        
        mp = {}
        n = len(nums)
        def f(pos):
            if pos >= n:return 0
            if pos in mp: return mp[pos]
            pick = nums[pos] + f(pos+2)
            ignore = f(pos+1)
            mp[pos] = max(pick, ignore)
            return mp[pos]
            
        
        return f(0)
        
        