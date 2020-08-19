'''https://leetcode.com/problems/numbers-with-same-consecutive-differences/'''
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        nums = [ i for i in range(10)]
        rst = []
        tmp = []
        pos = 0
        pre = None
        def f(rst, tmp,pos, pre):
            
            if pos == N :
                if N > 1 and tmp[0] == 0: return
                rst.append(int(''.join(str(x) for x in tmp)))
                return
            
            for item in nums:  
                if ( pos == 0) or ( pre is not None and abs(pre - item) == K):
                    tmp.append(item)
                    f(rst, tmp, pos + 1, item)
                    tmp.pop()    
            return rst
                
        return f(rst, tmp,pos, pre)
        