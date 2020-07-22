'''
https://www.interviewbit.com/problems/window-string/
'''
import collections
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):
		mp = collections.Counter(B)
		
		start , end = 0 , 0 
		min_v = len(A) + 1 
		pos = 0 
		
		amount = len(B)
		
		while end < len(A):
			
			if A[end] in mp:
				if mp[A[end]] > 0 :
					amount -= 1
				mp[A[end]] -= 1
			
				
			
			while amount == 0:
				print(start, end, mp, amount)
				if end - start + 1 < min_v:
					min_v = end - start + 1
					pos = start
				if mp[A[start]] in mp:
					mp[A[start]] += 1
					if mp[A[start]]  > 0:
						amount += 1
				start += 1
			
			end += 1
		if min_v == len(A) + 1 : return ""
		return A[pos: pos + min_v]