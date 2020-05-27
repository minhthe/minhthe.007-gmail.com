def solution(M, A):
	rst = 0 
	start = 0
	duplicate =  0
	n = len(A)
	mp = {}
	for i, v in enumerate(A):
		if v > M:
			rst += (i-start)*(i-start+1)//2
			start = i + 1
			continue
		if v not in mp:
			mp[v] = i
		else:
			if mp[v] >= start:
				
				rst += (i-start)*(i-start+1)//2
				start = mp[v] + 1
				if start < i:
					duplicate += (i - start) * (i - start + 1) //2 
			mp[v] = i
	rst += (n-start)*(n-start+1)//2				
	return rst - duplicate