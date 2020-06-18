'''
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
'''
import heapq
class Solution:
	def minSumOfLengths(self, arr: List[int], target: int) -> int:
		mp = {0:-1}
		rst = []
		s = 0
		for i , v in enumerate(arr):
			s += v
			if s - target in mp:
				start, end = mp[s-target] + 1 , i
				l =  end - start + 1
				rst.append(  (l , start , end) )
			mp[s]	= i 
		heapq.heapify(rst)
		def f(rst):
			n =len(rst)
			mm = int(1e9)
			flag = False
			for i in range(n-1):
				l, s , e = rst[i]
				for j in range(i+1, n):
					ll, ss, ee = rst[j]
					if(ss <= s <= ee or  ss <= e <= ee ):continue
					flag = True
					mm = min(mm, l + ll)                                            
			if flag:
				return mm
			else:
				return -1
					
		ans = f(rst)
		return ans