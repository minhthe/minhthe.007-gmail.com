'''
https://leetcode.com/problems/range-sum-query-immutable
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        if len(nums) > 0: self.prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSum.append( self.prefixSum[-1] + nums[i] )

    def sumRange(self, i: int, j: int) -> int:
        if len(self.nums) > 0:
            return self.prefixSum[j] - self.prefixSum[i-1] if i!= 0 else self.prefixSum[j]
        return 0


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)