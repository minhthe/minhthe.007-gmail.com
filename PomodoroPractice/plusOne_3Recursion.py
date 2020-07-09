'''
https://leetcode.com/problems/plus-one/
'''
class Solution:	
	def plusOne(self, digits: List[int]) -> List[int]:
		if digits[-1] < 9:
			digits[-1] +=1 
			return digits
		else:
			def f(pos):
				if pos == -1:
					return [1] + digits
				if digits[pos] < 9:
					digits[pos] += 1
					return digits
				else:
					digits[pos] = 0
					return f(pos-1)
			digits[len(digits) - 1] = 0
			return f(len(digits) -2)