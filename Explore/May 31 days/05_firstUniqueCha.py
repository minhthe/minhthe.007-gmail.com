'''
https://leetcode.com/problems/first-unique-character-in-a-string/

time complexity: O(n)
space complexity: O(n)
'''
class Solution:
	def firstUniqChar(self, s: str) -> int:
		mp = {}
		for c in s:
			mp[c]  = 1 if c not in mp else mp[c] + 1
		for i,v in enumerate(s):
			if mp[v] == 1: return i
		return -1