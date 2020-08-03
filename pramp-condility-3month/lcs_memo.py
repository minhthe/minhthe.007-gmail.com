class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		mp= {}
		@lru_cache(maxsize=None)
		def f(i,j):
			if i == len(text1) or j == len(text2): return 0 
			if text1[i] == text2[j]: return 1 + f(i+1,j +1)
			else : return max( f(i+1,j), f(i,j+1) )
		return f(0,0)