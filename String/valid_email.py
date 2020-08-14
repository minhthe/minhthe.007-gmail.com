'''https://leetcode.com/problems/unique-email-addresses'''
class Solution:
	def numUniqueEmails(self, emails: List[str]) -> int:
		rst = []
		
		def convert(s):
			tmp = ""
			p1,p2 = s.split("@")
			for c in p1:
				if c == "+":
					return tmp + "@" + p2
				if c == ".":
					continue
				tmp += c
			
			
			return tmp + "@" +p2
			
		for e in emails:
			e = convert(e)
			rst.append(e)
		
		return len(set(rst))