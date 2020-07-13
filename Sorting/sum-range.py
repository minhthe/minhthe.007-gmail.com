'''
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
'''
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        tmp = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums) +1):
                tmp.append(sum(nums[i:j]))
        
        tmp.sort()
        return sum(tmp[left - 1: right])