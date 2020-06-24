'''
https://leetcode.com/problems/implement-strstr/
'''
class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		a  = haystack
		b = needle
		
		la = len(a)
		lb = len(b)
		
		mpa =  0
		mpb = 0
		if la < lb : return -1
		if lb == 0: return 0
		for i in range(lb):
			mpa += ord(a[i])
			mpb += ord(b[i])
		for index in range(la - lb + 1 ):
			if mpa == mpb and a[index: index + lb  ] == b:
				return index
			end =   index + lb 
			if end < (la) : mpa += ord(a[index]) * (-1) + ord(a[end])
		return -1