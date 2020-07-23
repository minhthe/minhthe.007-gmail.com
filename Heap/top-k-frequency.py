'''
https://leetcode.com/problems/top-k-frequent-elements
'''
import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = collections.Counter(nums)
        
        rst = []
        
        for u,v in mp.items():
            heapq.heappush(rst, ( v, u )  )
            if len(rst) > k : 
                heapq.heappop(rst)
        return list(item[1] for item in rst[::-1])
        
        