'''
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #[1,1,0,0,1,1,1,0,1]
        mp = {}
        
        n = len(nums)
        k = len([x for x in nums if x == 1])
        if k == n :return n -1
        s = 0 
        pos = -1
        for i, v in enumerate(nums):
            s += v
            if v == 0:
                mp[i] = [s]
                
                
            
                if pos != -1:
                    mp[pos].append(s)
                s = 0
                pos = i
        if pos != -1: mp[pos].append(s)
        # print(mp)
        
        def f(mp):
            rst = 0
            for item in mp:
                rst = max(rst, sum(mp[item]))
            return rst
            
        return f(mp)