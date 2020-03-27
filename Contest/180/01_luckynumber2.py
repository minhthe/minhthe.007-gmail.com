'''
https://leetcode.com/problems/lucky-numbers-in-a-matrix
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        rmin = [min(item) for item in matrix]
        cmax = [max(item) for item in zip(*matrix)]
        return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if rmin[i] == cmax[j] ]
        
          
        
          