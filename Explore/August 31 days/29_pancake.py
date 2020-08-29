'''https://leetcode.com/problems/pancake-sorting/'''
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def reverse(A, k):
            # 1 2 3  4 5 ->5  4 3 2 1
            left ,right = 0, k
            while left < right:
                A[left], A[right] =  A[right], A[left]
                left, right = left + 1, right - 1
            return A
               
            
        rst = []
        for i in range(len(A) -1, -1, -1):
            max_v = max(A[:i+1])
            k = A[:i+1].index(max_v)
            # if k == 0:
            #     continue
            reverse(A,k)            
            rst.append(k+1)
            reverse(A,i)
            rst.append(i+1)
        return rst