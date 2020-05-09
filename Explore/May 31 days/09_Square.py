'''
https://leetcode.com/problems/valid-perfect-square/

'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1 , int(num ** (1/2)) + 1):
            if i *i == num:
                return True
        return False