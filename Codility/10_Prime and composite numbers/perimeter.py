def solution(N):
    # write your code in Python 3.6
    pass
    rst = int(4e9)  + 7  # this is important
    for i in range(  1, int(N**(0.5)) + 1):
        if N % i == 0:
            a = N // i
            b = N // a
            rst = min(rst , (a+b) * 2)
    return rst