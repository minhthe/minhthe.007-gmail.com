'''
https://leetcode.com/problems/top-k-frequent-elements/
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for item in nums:
            mp[item] = mp[item] + 1 if item in mp else 1
        rst = []
        for u,v in sorted(mp.items(), key = lambda x: x[1], reverse = True):
            if k == 0 :
                return rst
            rst.append(u)
            k-=1
        return rst