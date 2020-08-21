'''https://leetcode.com/problems/sort-array-by-parity'''
class Solution:
	def sortArrayByParity(self, A: List[int]) -> List[int]:
		arr = [[] for _ in range(2)] 
		for item in A:
			if item & 1: arr[1].append(item)
			else: arr[0].append(item)
		return arr[0] + arr[1]