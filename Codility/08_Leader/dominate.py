# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    mp = {}
    cnt = 0
    rst = -1
    for i, item in enumerate(A):
        mp[item] = 1 if item not in mp else mp[item] + 1
        if mp[item] > cnt:
            cnt = mp[item]
            rst = i
        cnt = max(cnt, mp[item])
    if cnt <= len(A)//2 : return -1
    else: return rst