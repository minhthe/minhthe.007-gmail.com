'''
https://leetcode.com/problems/build-an-array-with-stack-operations
'''
class Solution:
	def buildArray(self, target: List[int], n: int) -> List[str]:
		rst = []
		for i in range(1,n+1):
			rst.append('Push')
			if i not in target:
				rst.append('Pop')
			if i == target[-1]:
				return rst
		return rst