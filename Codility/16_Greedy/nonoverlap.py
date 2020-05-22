'''
https://app.codility.com/demo/results/training25QPSQ-BDD/
'''

def solution(A, B):
	n = len(A)
	if n < 2 : 
		return n
	period = []
	for i in range(n):
		period.append( (A[i], B[i]) )
		
	period.sort(key = lambda x : x[1])
	rst = 1
	tmp = period[0][1]
	for i in range(1, n):
		if period[i][0] > tmp:
			rst += 1
			tmp = period[i][1]
	
	return rst