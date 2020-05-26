'''https://app.codility.com/demo/results/trainingTVVAZB-A4P/
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    rst = set()
    
    for item in A:
        rst.add(abs(item))
    return len(rst)