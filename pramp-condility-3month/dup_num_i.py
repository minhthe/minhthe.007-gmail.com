'''https://leetcode.com/problems/contains-duplicate'''
import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        for item in c:
            if c[item] >= 2: return True
        return False