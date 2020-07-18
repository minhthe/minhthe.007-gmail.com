'''
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
'''
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            s = nums[i]
            arr.append(s)
            for j in range(i+1, n):
                s += nums[j]
                arr.append(s)
        return sum(sorted(arr)[left-1: right]) % int(1e9 + 7)