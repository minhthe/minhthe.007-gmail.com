def solution(N):
	#10000010001 
	start = 0
	
	
	rst = 0
	
	s = bin(N)[2:]
	for i in range(1, len(s)):
		if s[i] == '1':
			rst = max(rst, i - start -1)
			start = i 
	return rst