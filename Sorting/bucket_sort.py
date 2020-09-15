'''https://leetcode.com/problems/top-k-frequent-elements/'''
import collections
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		n = len(nums)
		mp = collections.Counter(nums)
		max_v = 0
		for key in mp:
			max_v = max(max_v, mp[key])
		rst= [[] for i in range(max_v+1)]
		for key in mp:
			rst[mp[key]].append(key)
		# print(rst)
		ans = []
		while k > 0:
			if(len(rst[max_v]) > 0):
				ans += rst[max_v]
				k -= len(rst[max_v])
			max_v -= 1
		return ans