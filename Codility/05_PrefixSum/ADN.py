def solution(S, P, Q):
	rst = []
	m = len(P)
	for i in range(m):
		u, v= P[i], Q[i]
		
		tmp = S[u:v+1]
		if 'A' in tmp:
			rst.append(1)
		elif 'C' in tmp:
			rst.append(2)
		elif 'G' in tmp:
			rst.append(3)
		else:
			rst.append(4)
	return rst