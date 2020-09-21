'''https://leetcode.com/problems/greatest-sum-divisible-by-three'''
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        s = sum(nums)
        if s % 3 == 0 : return s
        r1 = [item for item in nums if item%3 == 1]
        r2 = [item for item in nums if item%3 == 2]
        r1.sort()
        r2.sort()
        ans = [0]
        if s % 3 == 1:
            if r1:
                ans.append( s - r1[0] )
            if len(r2) >= 2:
                ans.append( s- sum(r2[:2]) )
        else:
            if r2:
                ans.append( s - r2[0] )
            if len(r1) >= 2:
                ans.append( s - sum(r1[:2]) )
        
        return max(ans)