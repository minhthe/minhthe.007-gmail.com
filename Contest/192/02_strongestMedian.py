class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        mp={}
        h = (n - 1 )// 2
        m = arr[h]
        for i,item in enumerate(arr):
            mp[i] = (abs(item - m), item )
        
        rst = []
        # print(mp)
        for item in sorted(mp.items(), key = lambda x:  x[1] ,  reverse = True):
            rst.append(item[1][1])
        
        # print(rst)
        return rst[:k]