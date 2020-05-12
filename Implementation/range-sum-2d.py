'''
https://leetcode.com/problems/range-sum-query-2d-immutable

'''
class NumMatrix:

	def __init__(self, matrix: List[List[int]]):
		self.M = matrix
		r = len(matrix) 
		if r > 0:
			c = len(matrix[0]) 
			self.prefixS = [[0 for i in range(c+1)]for j in range(r+1)]
			for i in range(1, r+1):
				for j in range(1, c+1):
					self.prefixS[i][j] +=  self.M[i-1][j-1] + self.prefixS[i-1][j] + self.prefixS[i][j-1] - self.prefixS[i-1][j-1]
		
	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		r1,r2,c1,c2 = row1+1, row2+1, col1+1, col2+1
		a =  self.prefixS[r2][c1-1] if c1 - 1 !=0 else 0
		b=  self.prefixS[r1-1][c2] if r1 - 1 !=0 else 0
		c =  self.prefixS[r1-1][c1-1] if c1 - 1 !=0 and r1 -1 != 0 else 0
		rst = self.prefixS[r2][c2]  - a - b + c
		return rst
		
		


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
