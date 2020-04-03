'''
https://leetcode.com/problems/ugly-number/

***Noting:
1 is typically treated as an ugly number.

'''
class Solution:
    def isUgly(self, num: int) -> bool:
        if num<=0: return False
        root = [2,3,5]
        for item in root:
            while(num%item == 0):
                num = int( num / item)
        return True if num == 1 else False