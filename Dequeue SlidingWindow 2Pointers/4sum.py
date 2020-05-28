'''
https://leetcode.com/problems/4sum/
'''
class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		n = len(nums)
		mp = {}
		nums.sort()
		rst = []
		for i in range(0, n-3):
			for j in range(n-1, 1, -1):
				a,b,c,d =i, i +1, j- 1, j
				while(b<c):
					s = nums[a] + nums[b] + nums[c] + nums[d]

					if s == target:
						tmp = [nums[a] , nums[b] , nums[c] , nums[d]] 
						tmp2 = tuple(tmp)
						if tmp2 not in mp:
							rst.append(tmp)
							mp[tmp2] = True
						b+=1 
						c-=1
					elif s < target:
						b += 1
					else:
						c -= 1
		return rst