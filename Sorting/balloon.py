'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        rst = []
        
        for u, v in sorted(points):
            if len(rst) and rst[-1][1] >= u:
                rst[-1][1] = min(rst[-1][1] , v)
            else:
                rst.append([u,v])

            
        return len(rst)