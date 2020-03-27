'''
https://leetcode.com/problems/largest-number-at-least-twice-of-others/

find the greatest number which is greater at least double of the rest elements on the array 
'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:            
        return nums.index(max(nums)) if len([x for x in nums if max(nums) >= x*2 ]) == len(nums) -1 else -1