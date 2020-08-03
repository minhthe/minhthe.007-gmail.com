'''
https://leetcode.com/problems/valid-palindrome-ii
'''
class Solution:
	def validPalindrome(self, s: str) -> bool:
		i,j = 0 , len(s)  -1
		
		
		def f1(i,j , flag):
		

			while(i<j):
				if(s[i]!= s[j]):
					if flag:
						i+=1
						flag = False
					else:
						return False
				else:
					i+=1
					j-=1
			return True
		def f2(i,j, flag):
		
			while(i<j):
				if(s[i]!= s[j]):
					if flag:
						j-=1
						flag = False
					else:
						return False
				else:
					i+=1
					j-=1			

			return True
		return f1(i,j,True) or f2(i,j,True)