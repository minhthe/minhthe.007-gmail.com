'''
https://leetcode.com/problems/detect-capital/
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 
        if word.lower() == word or word.upper() == word: return True
        if not ord('A')<=ord(word[0]) <= ord('Z'): return False
        for i in range(1, len(word)):
            if ord('A')<=ord(word[i]) <= ord('Z')  : return False
        return True