'''
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
'''
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        hh = [0] + sorted(horizontalCuts) + [h]
        ww =[0] + sorted(verticalCuts) + [w]
        m,n = 1,1
        for i in range(0, len(hh) -1):
            m = max( m, hh[i+1] - hh[i]  )
        
        for i in range(0, len(ww) -1 ):
            n = max( n, ww[i+1] - ww[i]  )
        
        return (m * n )% int(1e9+7)