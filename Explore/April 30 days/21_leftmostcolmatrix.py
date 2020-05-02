# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
            a = binaryMatrix
            rst = 101
            def f(i,j ,a):
                l, r = 0, j
                while(l<r):
                    
                    mid = (l+r)//2
                    
                    if(a.get(i,mid)):
                        
                        r = mid
                    else:
                        
                        l = mid + 1
                
                if(l!=j and a.get(i,l)):
                    return l
                return 101
                        
                
                
                
            r, c = a.dimensions()
            for i in range(r):
                rst = min(rst, f(i, c , a))
            return rst if rst  < 101 else -1
        
            
        
                