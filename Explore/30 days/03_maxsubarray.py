'''
https://leetcode.com/problems/maximum-subarray/

*** approach: divide and conquor
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def f2(nums, l, mid, r):
            ml = mr = -(1e9)
            sl = sr = 0
            for i in range(mid, l - 1, -1):
                sl += nums[i]
                if(sl > ml):
                    ml = sl
            for i in range(mid + 1, r+1, 1 ):
                sr +=nums[i]
                if(sr > mr):
                    mr = sr
            return ml + mr
        def f(nums, l ,r):
            if( l == r):
                return nums[l]
            mid = int( (r - l)/2 + l)
            max_left = f(nums, l, mid )
            max_right = f(nums, mid + 1, r)
            max_mid = f2(nums, l, mid , r)
            return max(max_left, max_right, max_mid)
            
        return f(nums, 0 , len(nums) -1)