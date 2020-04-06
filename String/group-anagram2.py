'''
https://leetcode.com/problems/group-anagrams
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rst = {}
        for item in strs:
            tmp = [0] * 26
            for c in item:
                tmp[ ord(c) - ord('a') ] += 1
            rst[tuple(tmp)] = [item] if tuple(tmp) not in rst else rst[tuple(tmp)] + [item]
        return rst.values()
                
        