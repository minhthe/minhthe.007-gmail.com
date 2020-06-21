class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        n = len(names)
        mp = {}
        rst = []

        def f(s):
            tmp = mp[s]
            tmp = s +"(" + str(tmp) + ")"
            while tmp in mp:
                # print(tmp)
                tmp = mp[s]  + 1
                tmp = s +"(" + str(tmp) + ")"
                mp[s] +=1 
            mp[tmp]= 1
            return tmp
            
            
        for item in names:
            if item not in mp:
                mp[item] = 1
                rst.append(item)
            else:
                rst.append( f(item) )
        return rst