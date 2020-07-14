'''
https://leetcode.com/problems/pancake-sorting

### code from pramp
def flip(arr,k):
  i, j = 0, k 
  while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i +=1 
    j -= 1
  return arr
  
  
def findMax(arr, p)  :
    pp = 0
    mx = -int(1e9)
    for i in range(0,p+1,1):
      if arr[i] > mx:
        mx = arr[i]
        pp= i
    return pp
def pancake_sort(arr):
  k = len(arr)
  
  for i in range(k -1 , -1, -1):
    mx = findMax(arr, i)
    if mx == i: continue
    rst = flip(arr, mx)
    rst = flip(arr, i)
  return arr
  

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