'''
https://leetcode.com/problems/search-suggestions-system
'''
import bisect
class Solution:
	def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
		rst = []
		products.sort()
		tmp = ""
		for c in searchWord:
			tmp += c
			p = bisect.bisect_left(  products, tmp  )	
			rst.append( [x for x in products[p:p+3 ]  if x.startswith(tmp)])
		return rst