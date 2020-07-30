'''
https://leetcode.com/problems/kth-largest-element-in-a-stream
'''
import heapq
class KthLargest:

	def __init__(self, k: int, nums: List[int]):
		self.nums = nums
		self.k = k
		heapq.heapify(self.nums)
		while(len(nums) > k):
			heapq.heappop(self.nums)
		
		
		

	def add(self, val: int) -> int:
		heapq.heappush(self.nums, val)
		if len(self.nums) > self.k:
			heapq.heappop(self.nums)
		return self.nums[0]