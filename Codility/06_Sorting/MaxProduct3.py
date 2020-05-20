def solution(A):
	#1  2 3 4 5 6 max of triple 
	A.sort()
	return max( A[0]* A[1] * A[-1],  A[-3]* A[-2] * A[-1])