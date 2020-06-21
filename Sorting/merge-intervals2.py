'''
https://leetcode.com/problems/merge-intervals/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        rst= []
        for item in sorted(intervals,key = lambda x : x[0]):
            if len(rst) and item[0] <= rst[-1][1]:
                rst[-1][1] = max( item[1], rst[-1][1]  )
            else:
                rst.append(item)
        return rst