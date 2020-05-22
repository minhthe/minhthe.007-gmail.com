'''
https://app.codility.com/demo/results/trainingMA7JDU-7K9/
->45%
'''
def solution(A):
	cnt = 0 
	n = len(A)
	if n < 3: return cnt 
	def check(a,b, c):
		x = a  + b > c
		y = c  + b > a
		z = a  + c > b
		return x and y and z
	
	tmp, rst , step = [], [] , 0
	def f(rst,tmp, step):
		cnt = 0 
		if ( len(tmp) == 3 and check(tmp[0], tmp[1],tmp[2])):
			return 1
		
		for i in range(step, n):
			tmp.append(A[i])
			cnt += f(rst,tmp, i+1)
			tmp.pop()
		return cnt
	return f(rst,tmp, step)