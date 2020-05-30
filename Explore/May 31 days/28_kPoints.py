'''
https://leetcode.com/problems/k-closest-points-to-origin

'''
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#        [[3,3],[5,-1],[-2,4]], K = 2
        mp = {}
        for item in points:
            u,v = item[0], item[1]
            d = u**2  + v** 2
            mp[(u,v)]=(d,u,v)
            
        rst = []
        cnt = 0 
        for item in sorted(mp.items() , key = lambda x: x[1]):
            cnt+=1
            tmp = [item[0][0], item[0][1]]
            rst.append(tmp)
            if cnt == K:
                return rst
        return rst