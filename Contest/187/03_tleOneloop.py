class Solution:
	def longestSubarray(self, nums: List[int], limit: int) -> int:
		i,j = 0,0
		n = len(nums)
		tmp = nums[j]
		rst = 1
		tmp2= nums[i]
		
		while(i < n and j < n):
			tmp = min(nums[i:j+1])
			tmp2 = max(nums[i:j+1]) 
			if( abs(tmp2 - tmp) <= limit):
				j += 1
				if j == n :
					rst = max(rst, j - i  )
			else:
				rst = max(rst, j - i  )
				i+=1
				
		return (rst)