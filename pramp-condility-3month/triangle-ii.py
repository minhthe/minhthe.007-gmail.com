'''https://leetcode.com/problems/pascals-triangle-ii/'''
class Solution:
	def getRow(self, k: int) -> List[int]:
		rst = [1]
		for i in range(1, k + 1):
			pos = 1
			tmp = rst[0]
			while pos != i :
				
				pre = rst[pos]
				
				rst[pos] += tmp
				
				tmp = pre
				
				pos += 1
			rst.append(1)
		return rst