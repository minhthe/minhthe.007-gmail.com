'''
https://app.codility.com/demo/results/trainingTEVAXX-8KG/
'''
def solution(A):
	cnt = 0 
	n = len(A)
	if n < 3: return cnt 
	A.sort()
# 	print(A)
	for i in range(n-1, 1, -1):
		left, right = 0, i -1
		while left < right:
# 			print(left, right)
			if A[left] + A[right] > A[i]:
				cnt = cnt +  (right - left ) 
				right -= 1
				
			else:
				left +=1 
	return cnt