def solution(A):	
	def f(A):
		a = []
		cnt = 0
		m = 0
		pos = 0
		mp = {}
		for item in A:
			mp[item] = 1 if item not in mp else mp[item] + 1
			if pos < mp[item]:
				m = item
				pos = mp[item]
			if item == m:
				cnt += 1
			else:
				cnt -= 1
			if cnt > 0:
				a.append(m)
			else:
				a.append('e')
		return a
		
		
	rst= f(A)
	
	
	rst2 = f(A[::-1])
	rst2 = rst2[::-1]
# 	print(rst)
# 	print(rst2)
	ans = 0
	for i in range(len(A) -1):
		if rst[i] == rst2[i+1] and rst[i] != 'e':
			ans += 1
	return ans