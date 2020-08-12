'''https://leetcode.com/problems/pascals-triangle-ii/'''
class Solution:
	def getRow(self, k: int) -> List[int]:
		rst = [ [] for i in range(k+1)]
		if k == 0: return [1]
		rst[0] = [1]
		rst[1] = [1,1]
		def f(arr):
			tmp = [1]
			for i in range(1, len(arr)):
				tmp.append( arr[i-1]  + arr[i])
			tmp.append(1)
			return tmp
			
		for i in range(2, k+1):
			rst[i] = f(rst[i-1])
		return rst[k]