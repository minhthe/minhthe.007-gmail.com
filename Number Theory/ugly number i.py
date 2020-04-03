'''
https://leetcode.com/problems/ugly-number/

if using sieve of prime will be TLE 
'''
class Solution:
    def isUgly(self, num: int) -> bool:
        root = [2,3,5]
        if num <= 0 : return False
        def f(num):
            if(num == 1):
                return 1
            for item in root:
                if(num % item == 0):
                    return f(int(num/item))
            return -1
        while(num!=1):
            num = f(num)
            if(num <= 0 ):
                return False
            
        return True
        