def solution(A):
    # write your code in Python 3.6
    pass
    n = len(A)
    cnt = 0 
    for i in range(n):
        if A[i] == 0:
            for j in range(i+1,n):
                if A[j] == 1:
                    cnt += 1
    return cnt if cnt <= int(1e9) else -1