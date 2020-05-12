'''
https://leetcode.com/problems/single-element-in-a-sorted-array/
'''
class Solution:
	def singleNonDuplicate(self, nums: List[int]) -> int:
		n = len(nums)
		if n==1: return nums[0]
		# n alway the odd number
		l , r = 0 , n - 1
		while(l<r):
			
			mid = int(  (r-l)/2  + l )
			if( nums[mid-1] != nums[mid] != nums[mid+1] ): return nums[mid]
			if mid & 1 : # le
				if nums[mid-1] == nums[mid]:
					l = mid + 1
				else:
					r = mid - 1
			else:
				if nums[mid +1] == nums[mid]:
					l = mid + 1
				else:
					r = mid - 1
		return nums[l]