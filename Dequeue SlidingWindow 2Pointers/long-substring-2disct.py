'''
https://www.lintcode.com/problem/longest-substring-with-at-most-two-distinct-characters/
'''
import collections		
class Solution:
	def lengthOfLongestSubstringTwoDistinct(self, s):
		# Write your code here
		if len(s) == 0 : return 0
		ss = set()
		frequency = collections.defaultdict(lambda:0)
		start = 0
		mx = 0
# 		print(ss,frequency )
		for end in range(len(s)):
# 			print(end)
			while len(ss) > 2:
				frequency[s[start]] -= 1  #print(s[start]) 
				if frequency[s[start]] == 0:
					ss.remove(s[start])
				start += 1
			frequency[s[end]] +=1
			ss.add(s[end])
			if len(ss) <= 2: mx = max(mx, end - start  + 1)
			
						
		return mx if len(ss) > 2 else max(mx, end - start  + 1)
		