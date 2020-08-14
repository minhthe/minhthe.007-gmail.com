'''https://www.lintcode.com/problem/palindrome-permutation/description'''
import collections
class Solution:    
	def canPermutePalindrome(self, s):
		c = collections.Counter(s)
		rst = 0 
		flag = False
		for item in c:
			if c[item] & 1 :
				flag = True
				rst += c[item] - 1
			else:
				rst += c[item]
		rst = rst + 1 if flag else rst
		return rst == len(s)