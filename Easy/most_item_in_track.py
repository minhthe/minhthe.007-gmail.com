'''https://leetcode.com/problems/most-visited-sector-in-a-circular-track/'''
import collections
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        
        # 2 step
        mp = collections.defaultdict(lambda : 0 )
        r = len(rounds)
        for i in range( r - 1):
            
            if i == 0 :
                u ,v = rounds[i], rounds[i+1]
                if u < v :
                    for j in range( rounds[i] , rounds[i+1] + 1, 1  ):
                        mp[ j ] += 1
                else:
                    for j in range( u , n+1, 1  ):
                        mp[ j ] += 1
                    for j in range( 1, v + 1, 1  ):
                        mp[ j ] += 1
                    
                    
            else:
                u ,v = rounds[i], rounds[i+1]
                if u < v :
                    for j in range( rounds[i] +1, rounds[i+1] + 1, 1  ):
                        mp[ j ] += 1
                else:
                    for j in range( u +1 , n+1, 1  ):
                        mp[ j ] += 1
                    for j in range( 1, v + 1, 1  ):
                        mp[ j ] += 1
                
        # print(mp)
        rst = [] 
        
        for u,v in sorted(mp.items(), key = lambda x: x[1], reverse= True):
            if len(rst) > 0 and mp[rst[-1]] != v:
                return sorted(rst)
            rst.append(u)
        rst.sort()
        # print('df',rst)
        return rst