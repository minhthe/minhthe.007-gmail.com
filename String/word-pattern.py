'''
https://leetcode.com/problems/word-pattern
'''
class Solution(object):
	def wordPattern(self, pattern, str):
		p = len(pattern)
		ss = str.split(" ")
		s = len(ss)
		if p != s : return False
		
		mp = {}
		mp2 = {}
		# print(ss)
		for i, v in enumerate(ss):
			tmp = pattern[i]
			if v in mp2:
				if tmp != mp2[v] : return False
			if tmp not in mp:
				mp[tmp]  = v
				mp2[v] = tmp
			else:
				if v != mp[tmp]: return False
		return True