class Solution:
	def isPalindrome(self, s: str) -> bool:
		i , j = 0 , len(s)  - 1
		
		def violate(c):
			if ord('a') <= ord(c) <= ord('z')  or  ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
				return False
			return True
		while i < j : 
			if violate(s[i]):
				i += 1
				continue
			if violate(s[j]):
				j -= 1
				continue
			if s[i].lower() != s[j].lower(): return False
			i+=1
			j-=1
		return True