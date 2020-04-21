'''
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

'''
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        table = {}
        dishes= set()
        
        for order in orders:
        
            i, j , k = order[0], order[1], order[2]
            
            if j not in table:
                table[j] = {}                   
            
            if k not in table[j]:
                table[j][k] = 1
            else:
                table[j][k] += 1
            
            dishes.add(k)
                
        dishes = list(dishes)
        dishes.sort()
        rst = [['Table'] + (dishes)]
        
        for item in sorted(table.items(), key = lambda x: int(x[0])  ):
            u, v= item[0], item[1]
            tmp = [u]
            for d in dishes:
                if(d in v):
                    tmp.append(str(v[d]))
                else:
                    tmp.append("0")
            rst.append(tmp)
        return rst
     