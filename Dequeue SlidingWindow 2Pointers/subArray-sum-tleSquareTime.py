'''
https://leetcode.com/problems/subarray-sum-equals-k
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        for i,v in enumerate(nums):
            presum[i+1] = v + presum[i]  
        cnt = 0 
        for i in range(n):
            for j in range(i+1, n+1):
                if( presum[j] - presum[i] == k):
                    cnt+=1
        return cnt