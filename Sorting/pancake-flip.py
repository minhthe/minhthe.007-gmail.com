'''
https://leetcode.com/problems/pancake-sorting
'''
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        # return [2,4,2,3]
        rst = []
        n = len(A)
        def find(A, nn):
            m = -int(1e9)
            pp = 0 
            
            for i in range(0, nn):
                if m < A[i]:
                    m = A[i]
                    pp = i
            # print(nn, pp)
            return pp + 1
        while(n > 1):
           
            pos = find(A, n)
            # print(A, pos)
            if pos == n :
                n = n -1 
                continue
            if pos == 1:
                A = A[:n][::-1] + A[n:]
                rst.append(n)
                n=n-1
                continue
         
            A = A[:pos][::-1] + A[pos:]
            A = A[:n][::-1]
            rst.append(pos)
            rst.append(n)
            n-=1
        return rst