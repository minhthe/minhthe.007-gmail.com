''''https://leetcode.com/problems/subarray-sum-equals-k'''
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		
		cnt = 0 
		
		tracking = defaultdict(int)
		s = 0 
		for item in nums:
			s+= item
			if s == k: cnt += 1
			if s- k in tracking: cnt += tracking[(s-k)]
			tracking[s] += 1 
				
		return cnt
