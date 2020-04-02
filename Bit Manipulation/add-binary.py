'''
https://leetcode.com/problems/add-binary/

'{0:08b}'.format(number) =  bin(number)[2:].zfill(8) 

'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tmp = int(a, 2)  + int(b, 2)
        def f(tmp):
            cnt = 0
            while(tmp):
                tmp = tmp// 2
                cnt +=1
            return cnt
        l = f(tmp)
        return bin(tmp)[2:].zfill(l) 