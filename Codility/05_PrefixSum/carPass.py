def solution(A):
    # write your code in Python 3.6
    pass
    # stk = []
    cnt_zero = 0
    rst = 0
    for item in A:
        # stk.append(item)
        if item == 0:
            cnt_zero += 1
        if item == 1:
            rst += cnt_zero
    return rst if rst <= int(1e9) else -1
