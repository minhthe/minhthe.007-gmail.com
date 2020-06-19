'''
https://leetcode.com/problems/longest-duplicate-substring/
'''
class Solution:
	def longestDupSubstring(self, S: str) -> str:
		l = len(S)
		mp = {}
		def f(k):
			hs = {}
			for i in range(l-k+1):
				tmp = S[i:i+k+1]
				# print(tmp)
				if tmp in hs:
				
					return True, tmp
				else:
					hs[tmp] = True
			return False, ""
		for i in range(l-1, -1, -1):
			
			flag , rst = f(i) 
			if flag:
				return rst
		return ""