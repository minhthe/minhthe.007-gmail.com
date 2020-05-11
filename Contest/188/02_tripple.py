'''
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
'''
class Solution:
	def countTriplets(self, arr: List[int]) -> int:
		ans = 0 
		rst = []
		
		def check(a):
			x = a[0] 
			for i in range(1, len(a)):
				x ^= a[i]
			return x == 0
			
		def f(arr, rst):
			k = 0
			for i in range(0, len(arr) -1 ):
				for j in range(i+2, len(arr)+1 ,1):
					tmp = arr[i:j]
					if(check(tmp)):
						k += len(tmp) -1
			return k
							
						
		
		ans = f(arr, rst)
		return ans