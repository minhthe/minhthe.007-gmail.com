'''
https://leetcode.com/problems/check-if-it-is-a-straight-line/

[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
[[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]

***careful with edge case: 0
'''
class Solution:
	def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
		ar = coordinates
		n = len(ar)
		if n <= 2 : return True
		
		#find the graph : y = ax + b
		#find a and b
		x1, y1 = ar[0][0],ar[0][1]
	
		x2, y2 = ar[1][0],ar[1][1]
		
		if (x2 - x1):
			a = ( y2 - y1) / (x2 - x1)
			b = y1 - a * (x1)
		else:
			b = y2 - y1
			a = y2 - b
		print(a,b)
		for i in range(2,n):
			u , v = ar[i][0], ar[i][1]
			if( v != u * a + b  ): return False
		return True