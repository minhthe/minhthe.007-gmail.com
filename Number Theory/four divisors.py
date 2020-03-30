'''
https://leetcode.com/problems/four-divisors/


***complexity:

time : O( N * log(M)) -> which M is the largest number of list N 
space : O(N ^ 2)
'''
class Solution:
	def sumFourDivisors(self, nums: List[int]) -> int:
		ans = 0 
		def f(num):
			s= set()
			for i in range(1, int(num ** (0.5)  ) + 1):
				if(num % i == 0):
					s.add(i)
					s.add(num//i)
					if(len(s) > 4): 
						break
			return sum(s) if(len(s) == 4) else 0
		for num in nums:
			ans += f(num)
		return ans