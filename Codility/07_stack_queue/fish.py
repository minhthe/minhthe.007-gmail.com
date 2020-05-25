def solution(A, B):	
	n = len(A)
	if n == 1: return 1
	stk = []
	p = n
	flag = True
	for i in range(n-1 , -1, -1):
		if B[i] == 0 :
			flag = False
			p  = i
			stk.append(  [ A[i], B[i]])
			break
		stk.append(  [ A[i], B[i]])
	if p == 0 or flag: return n 
	for i in range(p-1, -1, -1):
# 		print(stk)
		if B[i] == 0:
			stk.append( (A[i], B[i]))
			continue
		else:	
			while(  len(stk) and stk[-1][1] ==  0 and stk[-1][0] < A[i]  ):
				stk.pop()
			if( ( len(stk) and stk[-1][1] == 0 and stk[-1][0] > A[i]  ) ):
				continue
			stk.append( ( A[i],B[i] ) )
	return len(stk)