'''
https://leetcode.com/problems/lucky-numbers-in-a-matrix

'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        rst = []
        def check(i, j, matrix,R, C):
            #check row: is min
            val = matrix[i][j]
            for c in range(C):
                if(val>matrix[i][c]): return False
            for r in range(R):
                if(val<matrix[r][j]): return False
            return True
        for i in range(R):
            for j in range(C):
                if(check(i, j, matrix,R, C)):
                    rst.append(matrix[i][j])
        return rst