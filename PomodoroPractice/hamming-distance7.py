'''
https://leetcode.com/problems/hamming-distance/
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        rst = 0 
        for i in range(32):
            if x&1 ^ y&1: rst +=1
            x >>= 1 
            y >>= 1
        
        return rst