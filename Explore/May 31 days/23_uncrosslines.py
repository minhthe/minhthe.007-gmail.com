class Solution:
	def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
		m, n= len(A) , len(B)
		lcs = [[0 for i in range(n+1)] for j in range(m+1)]
		for i in range(1, m+1):
			for j in range(1, n +1):
				if A[i-1] == B[j-1]:
					lcs[i][j] = lcs[i-1][j-1] + 1
				else:
					lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
		return lcs[m][n]