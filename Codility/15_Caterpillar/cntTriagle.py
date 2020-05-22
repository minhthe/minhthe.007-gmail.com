'''
https://app.codility.com/demo/results/trainingDETY9Q-N8C/
-> 63%
'''
def solution(A):
	cnt = 0 
	n = len(A)
	if n < 3: return cnt 
	def check(a,b, c):
		x = A[a] + A[b] > A[c]
		y = A[c] + A[b] > A[a]
		z = A[a] + A[c] > A[b]
		return x and y and z
		
	for i in range(n-2):
		for j in range(i+1, n-1):
			for k in range(j + 1, n):
				if check(i, j ,k):
					cnt += 1
	return cnt