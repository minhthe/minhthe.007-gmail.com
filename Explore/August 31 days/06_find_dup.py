'''
https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''
import collections
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mp = collections.Counter(nums)
        # print(mp)
        rst = []
        for key in mp:
            if mp[key] ==2 : rst.append(key)
        return rst