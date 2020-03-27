'''
https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
'''
class Solution:
	def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
		cnt = len(arr1)
		for item in arr1:
			for item2 in arr2:
				if( abs(item - item2) <= d ): 
					cnt-=1
					break
		return cnt