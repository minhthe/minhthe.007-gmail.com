'''https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/'''
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        a = set( i for i in range(n))
        b = set(j for i , j in edges)
        c = list(a - b)
        return c