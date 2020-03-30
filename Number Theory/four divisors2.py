'''
https://leetcode.com/problems/four-divisors/
Based on the property of prime number to count the divisors:

n = p1 ^ (a1) * p2 ^ (a2) *... * pn ^ (an) ; (with p1,p2,..,pn is the prime)

= > the total divisors of number S = (a1+1) * (a2 + 1) * .. *(an +1)

***So if one number have 4 divisors we have 2 cases:

case 1: S = (a1+1) = (3 + 1) = 4 -> N = p1^3

case 2: S = (a1+1) * (a2 + 1) = 2 * 2 = 4 -> N = p1 ^ 1 * p2 ^ 1 ; (with p1,p2 is prime and p2!=p1 )
'''
def sieve(n):
	mark = [True] * (n + 1)
	mark[0] = False
	mark[1] = False
	for i in range(2, int(n **(0.5)) + 2):
		for j in range(i*i, n + 1, i):
			mark[j]  = False
	return mark 

class Solution:
	def sumFourDivisors(self, nums: List[int]) -> int:		
		mark = sieve(max(nums))
		
		def f(num, mark):
			s = 1 + num
			for i in range(2, int(num**(0.5))+1):
				if(i ** 3 == num):                    # case 1 :  n = p1 ^ 3 
					return s + i + num//i
				if(num % i == 0):
					s += i
					num = num//i
					if(mark[num] == True and num!=i):  # case 2 : n = p1 ^ 1 * p2 ^ 1 -> the "p2" must be prime and different with the "p1" 
						return s + num
					return 0
			return 0
					
		ans = 0		
		for num in nums: 
			ans += f(num, mark)
		return ans