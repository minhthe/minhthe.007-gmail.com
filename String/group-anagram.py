'''
https://leetcode.com/problems/group-anagrams/
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rst = []
        mp = {}
        for item in strs:
            tmp = ''.join(sorted(item))
            mp[tmp] = [item] if tmp not in mp else mp[tmp] + [item]
        for key in mp:
            rst.append(mp[key])
        return rst
            
        