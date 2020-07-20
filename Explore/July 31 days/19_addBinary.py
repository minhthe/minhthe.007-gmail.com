'''
https://leetcode.com/problems/add-binary/
''''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(  bin(int(b,2)+ int(a,2))[2:]  )