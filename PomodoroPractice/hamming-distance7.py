'''
https://leetcode.com/problems/hamming-distance/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return len([ (u,v) for u,v in zip( bin(x)[2:].zfill(32), bin(y)[2:].zfill(32)  ) if u!=v ])
        
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        rst = 0 
        for i in range(32):
            if x&1 ^ y&1: rst +=1
            x >>= 1 
            y >>= 1
        
        return rst