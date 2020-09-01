'''https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product'''
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        arr = []
        k = []
        for kk in nums:
            if kk == 0 :
                arr.append(k)
                k =[]
            else:
                k.append(kk)
        if len(k): arr.append(k)
        rst =  0
        def getMax(num):
            cnt =  0 
            track = []
            for i, u in enumerate(num):
                if u < 0 :
                    cnt +=1
                    track.append(i)
            if cnt & 1 == 0 : return len(num)
            else:
           
                
                return max(  max(track[0] ,len(num) -( track[0] + 1 )),max(track[-1] ,len(num) -( track[-1] + 1 ))  )
                             
                        
        for item in arr:
            rst = max(rst, getMax(item))
        return rst
        
        
        