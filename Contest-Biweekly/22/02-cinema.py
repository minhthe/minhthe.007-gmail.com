'''
https://leetcode.com/problems/cinema-seat-allocation/
'''
class Solution:
	def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
		a = reservedSeats
		a.sort(key = lambda x: x[0])
		
		cnt_max = 2 * n
		mp = {}
		for item in a :
			if(item[0] in mp):
				mp[item[0]].append(item[1])
			else:
				mp[item[0]] = [item[1]]
		def f(arr):			
			if(len([x for x in arr if x in range(2,10)])== 0 ): return 0
			if(len([x for x in arr if x in range(4,8)]) == 0 or len([x for x in arr if x in range(2,6)]) == 0  or len([x for x in arr if x in range(6,10)]) == 0 ): return 1
			return 2
			
		for key in mp:
			arr = mp[key]
			cnt_max -= f(arr)
		return cnt_max