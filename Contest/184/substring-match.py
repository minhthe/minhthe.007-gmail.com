'''
https://leetcode.com/problems/string-matching-in-an-array
'''
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rst = []
        for i in range(len(words)):
            for j in range(len(words)):
                if( i ^ j and words[i] in words[j]):
                    rst.append(words[i])
                    break
        return rst