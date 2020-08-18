'''https://leetcode.com/problems/minimum-operations-to-make-array-equal/'''
class Solution:
	def minOperations(self, n: int) -> int:
		
		first = 1
		last = (n-1)*2 + first
		s  = n*(first + last) // 2
		
		target =  s   // n
		
		rst = 0 
		for i in range(n//2):
			number = (2 * i) + 1 
			rst += abs(number - target)
		return rst