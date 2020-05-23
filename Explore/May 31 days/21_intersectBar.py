'''
https://leetcode.com/problems/interval-list-intersections
'''
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        a , b= len(A) , len(B)
        i, j = 0, 0
        rst = []
        
        while i < a and j < b:
            
            aa = A[i]
            bb = B[j]
            
            aa_a, aa_b, bb_c, bb_d = aa[0], aa[1], bb[0], bb[1]
            if aa_b < bb_c or aa_a > bb_d:
                if aa_b > bb_d:
                    j += 1
                else :
                    i +=1 
                # i+=1
                # j+=1
                continue
            else:
                u , v =  max(aa_a, bb_c), min(aa_b, bb_d)
                rst.append([u, v])
                
                if i +1 < a:
                    uu = A[i+1][0]
                    if aa_b <= bb_d and bb_d >= uu:
                        i+=1
                        continue
                if j + 1 < b: 
                    vv = B[j+1][0]
                    if aa_b>=  bb_d and aa_b >= vv:
                        j+=1
                        continue
                i+=1 
                j+=1
        
                
            
        
            
        return rst