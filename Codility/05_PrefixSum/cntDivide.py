def solution(A, B, K):
	rst = (B//K) - (A//K) 
	return rst + 1 if A%K == 0 else rst 