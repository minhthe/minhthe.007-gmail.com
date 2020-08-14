'''https://leetcode.com/problems/longest-palindrome'''
import collections
class Solution:
	def longestPalindrome(self, s: str) -> int:
		c = collections.Counter(s)
		rst = 0
		hasOdd = False
		for item in c:
			if c[item] & 1:
				rst += c[item] - 1
				hasOdd = True
			else: rst += c[item]
		return rst + 1 if hasOdd else rst