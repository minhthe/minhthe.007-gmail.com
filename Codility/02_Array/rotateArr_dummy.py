def solution(A, K):
	
	n = len(A)
	
	if n < 2 or K == 0: return A
	rst = [0] * (n)
	
	for i in range(n):
		rst[ (i+ K) % n] = A[i]
	return rst