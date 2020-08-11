'''https://leetcode.com/problems/excel-sheet-column-number'''
class Solution:
	def titleToNumber(self, s: str) -> int:
		
		rst = 0 
		for c in s:
			rst = rst * 26   + (ord(c) - ord('A') + 1)
		return rst