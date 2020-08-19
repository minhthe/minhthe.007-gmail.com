'''
https://leetcode.com/problems/maximum-swap
'''
class Solution:
	def maximumSwap(self, num: int) -> int:
		
		tmp = list(str(num))
		n = list(str(num))
		n.sort(reverse = True)
		def f(item):
			for i in range(len(tmp)-1, -1, -1):
				if tmp[i] == item:
					return i
			return 0
		for i,v in enumerate(n):
			if v != tmp[i]:
				pos = f(v)
				tmp[i],tmp[ pos ] = tmp[pos  ],tmp[ i]
				return int(''.join(tmp))
		return int(''.join(tmp))