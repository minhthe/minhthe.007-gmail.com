'''
https://leetcode.com/problems/possible-bipartition/
'''
class Solution:
	def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
		graph = [ [] for i in range(N)  ] 
		for item in dislikes:
			u, v= item[0], item[1]
			graph[u-1].append(v-1)
			graph[v-1].append(u-1)
		print(graph)
		visited = [False] * (N)
		A = {}
		B = {}
		def f(p):
			stk = [(p, 'N')]
			while(len(stk)):
				u , v = stk.pop()
				visited[u] = True
				if v == 'N':
					A[u] = True
				else:
					if v=='A':
						if u in A: return False
						else: B[u] = True
					if v =='B' :
						if u in B: return False
						else: A[u] = True
				for ne in graph[u]:
					if u in A:
						if ne in A : return False
						if ne not in B: stk.append( ( ne, 'A' ) )
						B[ne] = True
						
					elif u in B:
						if ne in B: return False
						if ne not in A:stk.append( ( ne, 'B' ) )
						A[ne] = True
						
			return True
						
					
					
				
		for i in range(N):
			if visited[i] == False:
				if f(i) == False:
					return False
		return True