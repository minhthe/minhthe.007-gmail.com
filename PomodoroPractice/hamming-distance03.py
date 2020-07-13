'''
https://leetcode.com/problems/total-hamming-distance/
'''
class Solution:
	def totalHammingDistance(self, nums: List[int]) -> int:
		tmp = ["{0:032b}".format(item) for item in nums]
		tmp = zip(*tmp)	
		rst = 0
		for item in tmp:
			rst += item.count('0') * item.count('1') 
		return rst