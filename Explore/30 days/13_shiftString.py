'''
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/

'''
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        x, y = 0 , 0
        for item in shift:
            if item[0] == 0: x += item[1] 
            if item[0] == 1 : y += item[1]
        x = x % len(s)
        y = y % len(s)
        k = abs(x - y)
        if x > y : return  s[k:] + s[:k] 
        else: return   s[len(s) -k :] + s[:len(s) - k]
        