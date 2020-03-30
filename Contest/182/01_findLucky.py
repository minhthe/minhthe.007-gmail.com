'''
https://leetcode.com/problems/find-lucky-integer-in-an-array
'''
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mp ={}
        for num in arr:
            if num in mp :
                mp[num] += 1
            else:
                mp[num] = 1 
        ans = -1
        for key in mp:
            if mp[key] == key:
                ans = max(ans, key)
        return ans
        