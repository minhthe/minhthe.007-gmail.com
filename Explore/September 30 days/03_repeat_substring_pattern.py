'''https://leetcode.com/problems/repeated-substring-pattern'''
class Solution:
	def repeatedSubstringPattern(self, s: str) -> bool:
		
		n = len(s)
		def check(sub, pos, l):
			if pos == n: return True
			if s[pos: pos+l] != sub: return False
			return check(sub, pos+l, l)
		for i in range(1, n):  # 1, 2 
			tmp = s[:i]  # tmp = ab
			if check(tmp,i, i): return True		
		return False