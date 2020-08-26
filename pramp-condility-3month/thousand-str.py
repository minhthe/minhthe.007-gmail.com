'''https://leetcode.com/problems/thousand-separator/'''
class Solution:
	def thousandSeparator(self, n: int) -> str:
		n = str(n)
		n = n[::-1]
		return '.'.join( n[i:i+3] for i in range(0, len(n), 3 )   )[::-1]