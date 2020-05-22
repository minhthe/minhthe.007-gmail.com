'''
https://app.codility.com/demo/results/trainingFBGHFX-KF8/
'''
def solution(N):
	start = 0
	rst = 0
	flag = False
	for i in range(32):
		if (N >> i & 1 ): 
			if flag:
				rst = max(rst, i - start - 1)
			start = i
			flag = True
	return rst	
	