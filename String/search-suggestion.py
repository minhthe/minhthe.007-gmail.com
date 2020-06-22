'''
https://leetcode.com/problems/search-suggestions-system/
'''
import bisect
class Solution:
	def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
		products.sort()
		rst = []
		pos = 0 
		prefix = ""
		for c in searchWord:
			prefix += c
			pos = bisect.bisect_left(products, prefix, pos)
			rst.append([ x for x in products[pos : pos + 3] if x.startswith(prefix) ]) 
		return rst