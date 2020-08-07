'''https://leetcode.com/problems/valid-anagram/'''
import collections
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		ss = collections.Counter(s)
		tt = collections.Counter(t)
		if len(s) != len(t): return False
		for key in ss:
			if ss[key] != tt[key]: return False
		return True