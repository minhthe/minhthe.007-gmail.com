'''
https://leetcode.com/problems/counting-bits/
'''
class Solution:
	def countBits(self, num: int) -> List[int]:
		rst = []
		def f(n):
			cnt = 0 
			for i in range(33):
				if n >> i & 1:
					cnt+=1 
			return cnt
		for i in range(0, num+1):
			rst.append(f(i))
		return rst
