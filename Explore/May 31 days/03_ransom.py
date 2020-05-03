class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        root = {}
        ransom = {}
        for s in magazine:
            root[s] = 1 if s not in root else root[s] + 1
        for c in ransomNote:
            ransom[c] = 1 if c not in ransom else ransom[c] + 1
            if c not in root: return False
            if c in root and ransom[c] > root[c]:
                return False
        return True