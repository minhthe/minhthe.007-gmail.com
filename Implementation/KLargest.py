'''
https://leetcode.com/problems/kth-largest-element-in-a-stream
'''
import bisect
class KthLargest:

	def __init__(self, k: int, nums: List[int]):
		self.nums =  sorted(nums)
		self.k = k

	def add(self, val: int) -> int:
		pos = bisect.bisect_left(self.nums, val)
		self.nums.insert(pos, val)
		return self.nums[-self.k]
				