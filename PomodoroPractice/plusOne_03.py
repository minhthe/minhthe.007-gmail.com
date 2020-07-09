'''
https://leetcode.com/problems/plus-one/
'''
class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		tmp = ''.join(str(x) for x in digits)
		rst = int(tmp) + 1
		return [int(x) for x in list(str(rst))]