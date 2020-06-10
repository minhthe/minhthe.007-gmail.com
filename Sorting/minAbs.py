'''
https://leetcode.com/problems/minimum-absolute-difference/
'''
class Solution:
	def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
		mp = {}
		arr.sort()
		for i, v in enumerate(arr):
			if i + 1 == len(arr):
				break
			diff = arr[i+1] - v
			if diff not in mp:
				mp[diff] = [ [v, arr[i+1]] ]
			else:
				mp[diff].append( [v, arr[i+1]] )
		
		for item in sorted(mp.items(), key = lambda x : x[0]):
			return item[1]
		return []