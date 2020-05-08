'''
https://leetcode.com/problems/minimum-size-subarray-sum/
'''
import collections
class Solution:
	def minSubArrayLen(self, s: int, nums: List[int]) -> int:
		
		de = collections.deque([])
		i, tmp = 0, 0 
		rst = len(nums) + 1
		for j in range(len(nums)):
			tmp += nums[j]
			de.append(j)
			while(tmp >= s):
				rst = min(rst, len(de))	
				tmp -= nums[i]
				de.popleft()				
				i += 1
				
			
		return rst if rst <= len(nums) else 0