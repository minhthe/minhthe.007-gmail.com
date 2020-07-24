'''
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums
'''
import heapq
import collections
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        pq = list( (v, i) for i,v in enumerate(nums))
        m = int(1e9 + 7)
        heapq.heapify(pq)
        rst = 0
        for k in range(right):
            v, i = heapq.heappop(pq)    
            if k >= left - 1:
                rst += v % m
            if i==n-1:
                continue
            vv = v + nums[i+1]
            heapq.heappush(pq, (  vv, i + 1 )  )
        return rst % m