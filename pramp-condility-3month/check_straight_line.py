'''https://leetcode.com/problems/check-if-it-is-a-straight-line/'''
class Solution:
	def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
		
		special = True
		for i,item in enumerate(coordinates):
			if i == 0: continue
			if coordinates[i-1][0] !=item[0] :
				special = False
		if special: return True
 
		co_constant = None
		
		
		for i in range(1, len(coordinates)):
			u, v= coordinates[i], coordinates[i-1]
			ux,uy,vx,vy = u[0], u[1], v[0], v[1]
			if ux - vx == 0 : return False
						
			if co_constant is None:
				co_constant = ( (uy-vy)/(ux-vx) )
				continue
			
			co_current = ( (uy-vy)/(ux-vx) )
			if co_current!= co_constant: return False
		return True	