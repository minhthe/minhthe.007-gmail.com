'''
https://leetcode.com/problems/jewels-and-stones/
'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        mp = {}
        for j in J:
            mp[j] = 1 if j not in mp else mp[j] + 1
        rst = 0 
        for s in S:
            if s in mp:
                rst += 1
        return rst