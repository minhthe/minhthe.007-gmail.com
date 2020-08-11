'''https://leetcode.com/problems/excel-sheet-column-title/'''
class Solution:
	def convertToTitle(self, n: int) -> str:
		
		rst = ""
		
		while n > 0:
			n = n -1
			t = n % 26 
			rst+= chr(t  + ord('A')  )
			n =  n//26
		return rst[::-1]