'''https://leetcode.com/problems/maximum-number-of-coins-you-can-get/'''
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        k = n // 3
        piles.sort()
        rst = 0 
        p = n - 2
        while k > 0 :
            rst += piles[p]
            p -= 2
            k -= 1
            
        return rst