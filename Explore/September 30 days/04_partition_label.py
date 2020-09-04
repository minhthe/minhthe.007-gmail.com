'''https://leetcode.com/problems/partition-labels/'''
class Solution:
	def partitionLabels(self, S: str) -> List[int]:
		n  = len(S)
		mp = {}
		for i in range(n):
			if S[i] not in mp:
				mp[S[i]] = [i, i]
			else:
				mp[S[i]][1] = i
		left, right = mp[S[0]][0], mp[S[0]][1]
		parts =  []
		#ababcbacadefegdehijhklij
		#abcdab
		cnt = 1
		while right  < n:
			if left == right and right < n : 
				parts.append(cnt)
				cnt = 1
				if right+1 < n : left, right = mp[S[right+1]][0], mp[S[right+1]][1]
				else: break
			else:
				left1, right1 = mp[S[left+1]][0], mp[S[left+1]][1]
				if right1 > right: right = right1
				left += 1
				cnt+=1
			
		return parts
		