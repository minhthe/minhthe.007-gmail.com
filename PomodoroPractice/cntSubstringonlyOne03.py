'''
https://leetcode.com/problems/number-of-substrings-with-only-1s
'''
class Solution:
    def numSub(self, s: str) -> int:
        return sum( list(  len(item) * (len(item)  +1) //2  for item in s.split("0")  ) ) % int(1e9+7)