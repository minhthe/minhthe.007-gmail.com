'''
https://leetcode.com/problems/3sum-closest

***more practice: codility -> abs slice :
https://app.codility.com/demo/results/trainingB469SN-3M3/
'''
class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		n  = len(nums)
		nums.sort()
		s = nums[0] + nums[1] + nums[n-1]
		ans = s
		rst = int(1e9)
		for i in range(0, n-1):
			left, right = i+1, n - 1
			while(left<right):
				t = nums[i] + nums[left] + nums[right]
				if t > target  :
					right -= 1
				else:
					left += 1
				if abs(target -  t) < abs(target - ans):
					ans = t
		return ans