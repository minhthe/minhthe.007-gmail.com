'''
https://leetcode.com/problems/sort-characters-by-frequency/
'''
class Solution:
	def frequencySort(self, s: str) -> str:
		mp = {}
		for e in s:
			if e not in mp:
				mp[e] = [1, ord(e) * (-1)]
			else:
				mp[e][0] +=  1
		rst = []
		# print(mp)
		for item in sorted(mp.items(), key = lambda x : x[1], reverse = True):
			for i in range( item[1][0] ):
				rst.append(  chr( item[1][1] * (-1))  )
		# print(rst)
		return ''.join(rst)