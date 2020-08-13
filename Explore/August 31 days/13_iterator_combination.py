'''https://leetcode.com/problems/iterator-for-combination/'''
def f( start,rst,  tmp, s, n):
	if len(rst) == 10000: return rst
	if len(tmp) == n:
		rst.append(''.join(tmp))
	if len(tmp) < n:	
		for i in range(start, len(s)):
			tmp.append(s[i])
			f(i+1, rst ,  tmp,s, n)
			tmp.pop()
	return rst
class CombinationIterator:


			
	def __init__(self, characters: str, combinationLength: int):
		self.rst = f(0,[], [], characters, combinationLength )
		self.pos = 0
	
	def next(self) -> str:
		self.pos +=1 
		return self.rst[self.pos - 1]
		
		

	def hasNext(self) -> bool:
		return  self.pos < len(self.rst)