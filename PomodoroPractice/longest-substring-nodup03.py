'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		
		ss = set()
		start = 0
		rst = 0
		for end in range(len(s)):
			if s[end] in ss:
				while(s[end] in ss):
					ss.remove(s[start])
					start +=1
			ss.add(s[end])
			#print(start ,end , ss)
			rst = max(rst, end - start + 1)
		return rst