'''
https://leetcode.com/problems/search-suggestions-system/
'''

import bisect
class Solution:
	def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
		products.sort()   # NLogN
		prefix = ""
		rst = []
		for c in searchWord:  # M  * log N 
			prefix += c
			pos = bisect.bisect_left(products, prefix)
			rst.append(  [x for x in products[pos: pos + 3 ]  if x.startswith(prefix) ])
		
		return rst