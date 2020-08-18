'''https://leetcode.com/problems/top-k-frequent-elements/

[1,1,1,2,2,3]
2
[1]
1
[-1,-1]
1
[1,2]
2
[4,1,-1,2,-1,2,3]
2


[[], [3], [2], [1], [], [], []]
[[], [1]]
[[], [], [-1]]
[[], [1, 2], []]
[[], [4, 1, 3], [-1, 2], [], [], [], [], []]

'''
import collections
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		n = len(nums)
		rank = [[] for _ in range(n+1)]
		c = collections.Counter(nums)
		for key,value in c.items():
			rank[value].append(key)
		rst = []
		# print(rank)
		for i in range(n, -1, -1):
			if k and rank[i]:
				for item in rank[i]:
					rst.append(item)
				k -= len(rank[i])
		return rst