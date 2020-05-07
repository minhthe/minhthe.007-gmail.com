'''
https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

***TLE with 14 / 15 test cases passed.
'''
class Solution:
	def minSubArrayLen(self, s: int, nums: List[int]) -> int:
		i , j = 0, len(nums)-1
		memo = {}
		def f(i, j, nums, memo):
			if (i,j) in memo: return memo[(i,j)]
			if sum(nums[i:j+1]) < s: 
				memo[(i,j)] = int(1e9)
				return memo[(i,j)]
			if i==j and nums[i] >= s: 
				memo[(i,j)] = 1
				return memo[(i,j)]
			if i > j : 
				memo[(i,j)] = int(1e9)
				return int(1e9)									
			a = min(f(i, j - 1, nums, memo), f(i+1, j, nums, memo))
			memo[(i,j)] = a 
			if i!=j :
				b = j - i + 1			
				memo[(i,j)] = min(a,b)
			return memo[(i,j)]
		ans = f(i, j , nums, memo)
		#print(ans)
		#print(memo)
		return ans if ans < int(1e9) else 0