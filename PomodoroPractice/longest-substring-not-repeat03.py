'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
import collections
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		rst = collections.deque([])
		mp = collections.defaultdict(lambda : 0 )
		start = 0 
		mx = 0
		for end in range(len(s)):
			rst.append(s[end])
			mp[s[end]] +=1
			while mp[s[end]] > 1 :				
				rst.popleft()
				mp[s[start]] -= 1
				start += 1
			mx = max(mx, len(rst))
				
		return max(mx, len(rst))