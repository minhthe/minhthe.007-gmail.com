'''
https://leetcode.com/problems/search-suggestions-system
'''
import bisect
class Solution:
	def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
		
		products.sort()
		
		rst = []
		tmp = ""
		for c in searchWord:
			tmp += c
			pos = bisect.bisect_left(products, tmp)
			
			rst.append([x for x in products[pos : pos + 3] if x.startswith(tmp)]  )
		
		return rst
		