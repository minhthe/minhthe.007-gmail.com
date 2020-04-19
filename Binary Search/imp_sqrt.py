'''
https://leetcode.com/problems/sqrtx/

2 importance points:

1) initilize array A will be TLE with x greater 1e9
2) if in edge case l = 0 or l = 1 -> return that value

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # a = [i for i in range(0, int(x/2) + 1)]
        l , r = 0,  int(x/2)  
        while(l<=r):
            mid = int( (r - l)/2 + l )
            if( mid * mid  == x): return mid
            if mid * mid > x: r = mid - 1
            else: l = mid + 1
        return l - 1 if l > 1 else l   
        
        