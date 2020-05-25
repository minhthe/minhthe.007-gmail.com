''''
https://app.codility.com/demo/results/trainingQB99KZ-8YJ/
'''

def solution(A):
	rst = 0
	cnt = 0 
	n = len(A)
	for i in range(n-1, -1, -1):
		if A[i] == 1:
			cnt+=1
		if A[i] == 0:
			rst += cnt
	return rst if rst <= int(1e9) else - 1