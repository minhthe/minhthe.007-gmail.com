'''
https://leetcode.com/problems/count-number-of-teams/

'''
class Solution:
	def numTeams(self, rating: List[int]) -> int:
		def f(rating, tmp, step, cnt):
			if( len(tmp) == 3  and  ( (tmp[0] < tmp[1] < tmp[2] ) or (tmp[0]> tmp[1] > tmp[2]) )  ):
				cnt[0] +=1
			if(len(tmp)<3):
				for i in range(step, len(rating)):
					tmp.append(rating[i])
					f(rating, tmp, i+1, cnt)
					tmp.pop()
				return cnt[0]
		return f(rating, [], 0, [0])