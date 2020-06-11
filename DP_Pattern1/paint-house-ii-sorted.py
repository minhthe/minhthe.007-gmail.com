'''
https://www.lintcode.com/problem/paint-house-ii

***Time complexity: O( N * K log(K) )
'''
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        n = len(costs)
        if n == 0: return 0
        
        k = len(costs[0])
        
        if n == 1: return min(costs[0])
        
        
        for row in range(1, n):
            tmp = sorted(costs[row-1])
            first, second = tmp[0], tmp[1]
            print(first, second)
            for col in range(k):
                costs[row][col]  =   costs[row][col] + first if costs[row -1][col]  != first else costs[row][col]  + second
        return min(costs[-1])