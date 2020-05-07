'''
https://leetcode.com/problems/majority-element/

***tle with this code:
return [x for x in nums if nums.count(x) > (len(nums) >> 1)][0]
'''

class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		mp = {}
		for item in nums:
			mp[item] = 1 if item not in mp else mp[item] + 1
		n = len(nums)
		for key in mp:
			if mp[key] > n>>1: return key
		