''''
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
''''
class Solution:
	def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
		diff = (max(arr) - min(arr) ) 
		if diff % (len(arr) -1): 
			return False
		s = set(arr)
		mi = min(arr)
		gap = diff // (len(arr) - 1)
		for i in range(len(arr)-1):
			mi += gap
			if mi not in s:
				return False
		return True