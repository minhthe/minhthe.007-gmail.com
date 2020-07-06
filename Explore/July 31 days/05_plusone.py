'''
https://leetcode.com/problems/plus-one/
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = int(''.join(str(x) for x in digits))  + 1
        return list(int(x) for x in str(tmp)) 