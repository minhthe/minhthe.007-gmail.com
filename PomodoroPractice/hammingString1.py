'''
https://leetcode.com/problems/hamming-distance/
'''
class Solution:
	def hammingDistance(self, x: int, y: int) -> int:
		cnt = 0
		for i in range(32):
			if x&1 ^ y&1: cnt +=1
			x >>= 1
			y >>= 1
		return cnt