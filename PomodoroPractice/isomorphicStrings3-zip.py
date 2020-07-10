''''
https://leetcode.com/problems/isomorphic-strings
''''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len( set(zip(s,t)) ) == len(set(t)) == len(set(s))