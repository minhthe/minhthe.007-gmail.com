'''
https://leetcode.com/problems/two-sum/
'''
import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = collections.defaultdict(list)
        
        for i,v in enumerate(nums):
            mp[v].append(i)
        rst = []
        for item in nums:
            if target - item in mp:
                if len(mp[item] ) == 2: return mp[item]
                if mp[item][0]  != mp[ target - item ][0]:  
                    rst = [ mp[item][0]  , mp[ target - item ][0]  ]
                    break
        return rst
        