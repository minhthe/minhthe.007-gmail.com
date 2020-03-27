'''
https://leetcode.com/problems/kth-largest-element-in-an-array
'''
import heapq 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        tmp =[(-x) for x in nums]
        heapq.heapify(tmp)
        ans = -1
        for i in range(k):
            ans = heapq.heappop(tmp)
        return -ans
