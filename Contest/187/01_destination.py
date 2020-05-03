class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = {}
        k = {}
        for item in paths:
            u ,v = item[0], item[1]
            mp[v] = True
        for item in paths:
            u ,v = item[0], item[1]
            if u in mp:
                mp[u] = False
        for key in mp:
            if mp[key] == True:
                return key