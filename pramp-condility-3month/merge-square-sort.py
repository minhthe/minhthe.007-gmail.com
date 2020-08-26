'''https://leetcode.com/problems/squares-of-a-sorted-array/'''
class Solution:
	def sortedSquares(self, A: List[int]) -> List[int]:
		rst = []
		left = []
		right = []
		for item in A:
			if item < 0: left.append(item*item)
			else: right.append(item*item)
		
		left = left[::-1]
		while len(left)> 0 and len(right) > 0 :
			if left[0] < right[0]:
				rst.append(left[0])
				left.pop(0)
			else:
				rst.append(right[0])
				right.pop(0)
		for item in left:
			rst.append(item)
		for item in right:
			rst.append(item)
		return rst