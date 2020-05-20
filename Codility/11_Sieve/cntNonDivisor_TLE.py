def solution(A):
	rst = []
	m = max(A)
	n = len(A)
	for i in range(n):
		cnt = 0 
		for j in range(n):
			if i ^ j:
				if A[j] > A[i]: 
					cnt +=1
					continue
				if A[i] % A[j] != 0 :
					cnt = cnt + 1
		rst.append(cnt)
	return  rst