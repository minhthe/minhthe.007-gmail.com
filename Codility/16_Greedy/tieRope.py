'''
 https://app.codility.com/demo/results/training99RDJJ-WSK/
'''
def solution(K, A):
	n = len(A)
	#if n == 1:
	cnt = 0
	s = 0
	for i in range(n):
		s += A[i]
		if(s >= K):
			cnt+=1
			s = 0
	return cnt