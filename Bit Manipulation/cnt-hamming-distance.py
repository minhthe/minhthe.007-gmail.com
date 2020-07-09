'''
https://leetcode.com/problems/total-hamming-distance/
'''
class Solution:
	def totalHammingDistance(self, nums: List[int]) -> int:
		nums = ["{0:032b}".format(x) for x in nums]
		tmp = zip(*nums)
		rst = 0 
		for item in tmp:
			rst += item.count('0') * item.count('1')
		return rst