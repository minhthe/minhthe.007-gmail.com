'''
https://leetcode.com/problems/contiguous-array
'''
class Solution:
	def findMaxLength(self, nums: List[int]) -> int:
		mp  = {0:-1} #  -> very important : [0,1], [0,0,0,1,1,1]
		cnt = 0
		rst = 0
		for i, v in enumerate(nums):
			if v == 0: cnt -= 1
			else : cnt += 1
			if cnt in mp:
				rst = max(rst, i - mp[cnt])   # should be i - 1 - (mp[cnt] + 1) base on the balanced algorithm  
			else:
				mp[cnt] = i
		return rst