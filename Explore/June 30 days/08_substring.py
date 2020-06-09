'''
https://leetcode.com/problems/is-subsequence/
'''class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		ls, lt = len(s), len(t)
		
		if ls > lt: return False
		
		ss, tt = 0,0
		
		while ss < ls and tt < lt:
			if s[ss] == t[tt]:
				ss += 1
				tt += 1
			else:
				tt += 1
		return True if ss == ls else False