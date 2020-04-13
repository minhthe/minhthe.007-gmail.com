'''
https://leetcode.com/problems/string-matching-in-an-array

'''
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        return list(set( words[i] for i in range(n) for j in range(n)  if i ^ j and words[i] in words[j] )  )