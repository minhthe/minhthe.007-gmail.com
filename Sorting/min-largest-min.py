'''
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
'''
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4: return 0 
        print(nums)
        o0 = nums[-1] - nums[0]
        
        o1 = nums[-2] - nums[0]
        o11 = nums[-1] - nums[1]
        
        o2= nums[-1] - nums[2]
        o22= nums[-3] - nums[0]
        o222 = nums[-2] - nums[1]
        
        o3 = nums[-1]  - nums[3]
        o33= nums[-4] - nums[0]
        o333 = nums[-3]  - nums[1]
        o3333=nums[-2] - nums[2]

        
        return min(o1,o1,o11,o2,o22,o222,o3,o33,o333,o3333)