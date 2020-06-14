class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n  =len(arr)
        mp = {}
        for item in arr:
            mp[item] = 1 if item not in mp else mp[item]  + 1
        # print(mp)
        cnt = 0 
        for item in sorted(mp.items(), key = lambda x: x[1]):
            if k > 0 :
                k -= 1
                mp[item[0]] -= 1
                while k > 0 and mp[item[0]] > 0:
                    k-=1
                    mp[item[0]] -= 1
                if mp[item[0]] > 0:
                    cnt+=1
                
            else:
                if mp[item[0]] > 0:
                    cnt+=1
                
        return cnt