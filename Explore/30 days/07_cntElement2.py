'''
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/
'''
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        mp = {}
        for item in arr:
            mp[item] = mp[item] + 1 if item in mp else 1
            
        cnt = 0
        for key in mp:
            if(key + 1 in mp):
                cnt += mp[key]
        return cnt