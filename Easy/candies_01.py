'''https://leetcode.com/problems/distribute-candies-to-people'''
class Solution:
	def distributeCandies(self, candies: int, num_people: int) -> List[int]:
		n = num_people
		arr = [0] * (n)
		t = 0
		k = 0 
		while(candies > 0):
			for i,v in enumerate(arr):
				t = (i+1) + k*(n) 
				if candies > t:
					arr[i] = t + arr[i]
					candies -= t
					
				else :
					arr[i] += candies
					return arr
			k+=1		
		return arr