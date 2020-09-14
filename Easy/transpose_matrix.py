class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        r, c  =len(A), len(A[0])
        return [ [A[i][j] for i in range(r)] for j in range(c) ]