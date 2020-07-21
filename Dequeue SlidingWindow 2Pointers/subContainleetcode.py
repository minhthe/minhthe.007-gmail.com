'''
https://leetcode.com/problems/minimum-window-substring
'''
import collections
class Solution:
	def minWindow(self, s: str, t: str) -> str:
		
		mp = Counter(t)
		start, end = 0, 0 
		
		first = 0
		amount = len(t)
		mi = len(s)   + 1
		while end < len(s):
			if s[end] in mp:
				
				if mp[s[end]] > 0 :
					amount -= 1
				mp[s[end]] -= 1			
			while amount == 0 :
				
				if end - start + 1 < mi:
					mi = end - start  + 1
					first = start 
				if s[start] in mp:
					mp[s[start]] += 1
					if mp[s[start]] > 0:
						amount += 1
				
				start += 1			
			end += 1
		if len(s)  +1 == mi: return ""
		print(s[first: first + mi])
		return s[first: first + mi]