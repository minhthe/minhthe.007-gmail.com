'''
https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/d
'''
class Solution:
	def lengthOfLongestSubstringKDistinct(self, s, k):
		if len(s) == 0: return 0
		mp = {}
		start = 0 
		rst = 0 
		for end in range(len(s)):
			mp[s[end]] =  mp[s[end]]  + 1 if s[end] in mp else 1
			if len(mp) > k :
				rst = max(rst, end - start)
				while( mp[s[start]] != 0):
					mp[s[start]] -= 1
					if mp[s[start]] == 0: 
						del mp[s[start]]
						start += 1
						break
					start +=1

			
			
		return max(rst, end - start + 1)