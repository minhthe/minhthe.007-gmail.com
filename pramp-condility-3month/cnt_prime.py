'''https://leetcode.com/problems/count-primes/'''
class Solution:
	def countPrimes(self, n: int) -> int:
		primes = [1 for i in range(n+1)]
		
		for i in range(2, int(n**(0.5)) + 1 , 1):
			for j in range(i*i, n+1, i):
				primes[j] = 0
		return sum(primes[2:n])