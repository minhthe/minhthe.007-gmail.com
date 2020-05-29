'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		n = len(s)
		mp = {}
		rst = 0
		pos = 0 
		cnt = 0 
		if n == len(set([x for x in s])): return n 
		for i in range(n):
			if s[i] not in mp:
				cnt += 1
				mp[s[i]] = i
			else:
				if mp[s[i]] >= pos:
					cnt -=1
					rst = max(rst, i - pos  )
					pos = mp[s[i]] + 1
				mp[s[i]] = i
				
		rst = max(rst, n - pos)
		return rst