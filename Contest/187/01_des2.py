'''
https://leetcode.com/problems/destination-city/

Time Complexity : O(n)
Space Complexity : O(n)
'''
class Solution:
	def destCity(self, paths: List[List[str]]) -> str:
		des = {}
		root = {}
		for item in paths:
			start, end = item[0], item[1]
			root[start] = True
		
			if start in des:                         # if "start" is already in destination 
				del des[start]
				
			if end in root:                          # if  "end" is already in root and also in the desination
				if end in des:
					del des[end]
			else:
				des[end] = True
			
				
		return list(des.keys())[0]