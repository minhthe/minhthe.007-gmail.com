def solution(N):
	cnt = 0 
	for i in range(1,N + 1):
		if N % i == 0 :
			cnt+=1
	return cnt

  ## n // 2
  def solution(N):
	cnt = 0 
	for i in range(1,N//2  +1):
		if N % i == 0 :
			cnt+=1
	return cnt  +1 

  ### O(sqrt(N))
  def solution(N):
	cnt = 0
	for i in range(1, int(N ** (0.5)) + 1):
		if N % i == 0 :
			if N//i==i:
				cnt += 1
			else:
				cnt += 2
	return cnt