'''
https://leetcode.com/problems/number-complement/
'''
class Solution:
	def findComplement(self, num: int) -> int:
		
		#convet num - >to bit 
		x = bin(num)[2:]
		x = str(x[::-1])
		ans = 0
		for i,v in enumerate(x):
			if v == '0':
				ans += 2 **(i)
		return ans