'''
https://leetcode.com/problems/search-insert-position/
'''
class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		l ,r = 0 , len(nums) - 1
		def f(l , r ):
			while(l<=r):
				mid = int( (r- l) / 2 + l )
				if(nums[mid] == target) : return mid
				if (nums[mid] > target): r = mid - 1
				else: l = mid + 1
			return l
		return f(l , r )