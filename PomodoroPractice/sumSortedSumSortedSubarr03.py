'''
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums
'''
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        arr = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                arr.append(sum(nums[i:j]))
        return sum(sorted(arr)[left-1: right]) % int(1e9+7)
        