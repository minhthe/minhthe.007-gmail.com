'''https://leetcode.com/problems/decode-ways'''
class Solution:
	def numDecodings(self, s: str) -> int:
		@lru_cache(None)
		def f(pos):
		
			if pos >= len(s):return 1
			a, b =  0, 0
			
			if int(s[pos]) > 0 :
				if   pos + 1 == len(s) or ( pos + 1 < len(s) and int(s[pos+1])) > 0:
					a =  f(pos+1) 
					
			if int(s[pos]) > 0 and  pos + 1 < len(s) and int(s[pos:pos+2]) <= 26:
				b =  f(pos+2)
			return a + b
		return f(0)