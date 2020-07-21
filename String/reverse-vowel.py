'''
https://leetcode.com/problems/reverse-vowels-of-a-string/
'''
class Solution:
	def reverseVowels(self, s: str) -> str:
		vowels = ['a','e','o','u','i']
		i, j = 0 , len(s) - 1
		s = list(s)
		while i < j :
			flag = True
			if (s[i].lower()) not in vowels:
				i +=1
				flag = False
			if (s[j].lower()) not in vowels:
				j-=1
				flag = False
			if flag:
				s[i], s[j] =  s[j], s[i] 
				i+=1 
				j-=1
		return ''.join(s)