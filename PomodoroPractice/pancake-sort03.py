'''
https://leetcode.com/problems/pancake-sorting
'''

class Solution:
	def pancakeSort(self, A: List[int]) -> List[int]:
		n = len(A)
		def f(k):
			i , j = 0, k
			while i< j:
				A[i], A[j] = A[j], A[i]
				i += 1
				j-= 1
			return A
		rst = []
		def find(p):
			pp = 0
			mx = A[0]
			for i in range(1, p+1):
				if A[i] > mx:
					mx = A[i]
					pp = i
			return pp
			
		for i in range(n-1, -1, -1):
			p= find(i)
			if p == i : continue
			rst.append(p+1)
			f(p)
			rst.append(i+1)
			f(i)
		
		return rst