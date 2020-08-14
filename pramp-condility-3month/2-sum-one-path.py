class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		rst = []
		hs = {}
		for i, item in enumerate(nums):
			if target - item in hs:
				return [  hs[target - item] ,   i  ]
			hs[item] = i
		
		return rst