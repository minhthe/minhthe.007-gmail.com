'''
https://leetcode.com/problems/permutation-in-string/
'''

class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		# s1 = "ab" s2 = "eidbaooo"
		hs = {}
		for item  in s1:
			hs[item] = 1 if item not in hs else hs[item ] + 1 
		mp = {}
		
		flag = True
		cnt = 0 
		def f2(mp,hs):
			
			for key in hs:
				if key not in mp: return False
				if mp[key] != hs[key] : return False
			return True
			
		for i in range(len(s2)):
			cnt +=1
			if flag:
				mp[s2[i]] = 1 if s2[i] not in mp else mp[s2[i]] + 1  
				if(cnt % len(s1) == 0): 
					flag = False
			else:
				##
				pos = i - len(s1)
				mp[s2[pos]] -=1
				mp[s2[i]] =1 if s2[i] not in mp else  mp[s2[i]] + 1
				
			if(flag == False):
				if f2(mp, hs): return True
				
			
		
		
		return False