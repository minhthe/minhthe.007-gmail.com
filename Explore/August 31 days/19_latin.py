'''
https://leetcode.com/problems/goat-latin/
'''
class Solution:
	def toGoatLatin(self, S: str) -> str:
		
		tmp = list(item for item in S.split(" ") if len(item) > 0 )
		rst = []
		for i, item in enumerate(tmp):
			if item[0].lower() in ['a','e','o','u','i']:
				new_item = item + 'ma' + 'a' *(i+1)
			else:
				new_item = item[1:] + item[0] +  'ma' + 'a' *(i+1)
			rst.append(new_item)
		
		return ' '.join(rst)