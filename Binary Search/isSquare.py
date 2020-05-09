'''
https://leetcode.com/problems/valid-perfect-square/
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def f(num, l , r):
            while l<=r:
                mid = int( (r-l)/2 + l )
                if mid * mid == num: return True
                if mid * mid > num:
                    r = mid -1
                else:
                    l = mid + 1
            return False
        
        l, r = 1, num
        ans = f(num,l, r)
        return ans