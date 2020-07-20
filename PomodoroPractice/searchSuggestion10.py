'''
https://leetcode.com/problems/search-suggestions-system/submissions/
'''
import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        rst = []
        products.sort()
        tmp = ""
        for c in searchWord:
            tmp += c
            
            pos = bisect.bisect_left(products, tmp)
            
            rst.append( list(  item for item in products[pos: pos + 3] if item.startswith(tmp)  ))
        
        
        return rst