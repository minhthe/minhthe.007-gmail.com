'''
https://leetcode.com/problems/add-digits
'''
class Solution:
	def addDigits(self, num: int) -> int:
		tmp = list(str(num))
		s = 0 
		while(len(tmp) > 1):
			s = sum(int(item) for item in tmp)
			tmp = list(str(s))
		return tmp[0]