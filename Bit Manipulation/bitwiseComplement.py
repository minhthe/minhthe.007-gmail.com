'''

https://leetcode.com/problems/complement-of-base-10-integer/

*** or using formula based log:
from math import log
l = int(log(N, 2) -1) if N !=0 else 0

'''
class Solution:
	def bitwiseComplement(self, N: int) -> int:
		cnt = 1
		tmp  = N 
		while(tmp>= 2):
			cnt+=1
			tmp = tmp // 2
		return N ^ (2**cnt -1)