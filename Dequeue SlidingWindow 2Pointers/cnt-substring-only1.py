''''
https://leetcode.com/problems/number-of-substrings-with-only-1s/
'''
class Solution:
	def numSub(self, s: str) -> int:
		rst = 0 
		i = 0 
		k = 0 
		while(i < len(s)):
			if (s[i]== '0' ):
				rst += k * (k+1)//2
				k = 0 
				i +=1
			else:
				i+=1
				k+=1
			
		return (rst + k * (k+1)//2) % int(1e9 + 7)