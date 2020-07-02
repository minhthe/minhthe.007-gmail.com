''''
https://leetcode.com/problems/implement-strstr/
'''
  class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		h = len(haystack)
		n = len(needle)
		
		if n > h : return -1 
		
		if n == 0: return 0
		
		hh, nn = 0 , 0
		
		for i in range(n):
			hh += ord(haystack[i])
			nn += ord(needle[i])
		for i in range(h - n + 1):
			if hh == nn :
				if needle == haystack[i:i + n]  : return i
			if i + n < h: hh = hh + ord(haystack[i+n]) - ord(haystack[i])
		return -1
			