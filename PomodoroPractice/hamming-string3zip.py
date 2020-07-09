'''
https://leetcode.com/problems/hamming-distance/
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return len( [True for u, v in zip('{0:032b}'.format(x), '{0:032b}'.format(y))  if u!=v] )