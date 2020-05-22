'''
List these prime number that smaller 10
10 -> 2, 3, 5, 7 
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        mark = [True]*(n)
        if n <3 : return 0
        mark[0], mark[1] = False, False
        for i in range(2,int(n**(0.5)) +1 ):
            for j in range(i*i, n, i):
                mark[j] = False
        return len([x for x in mark if x == True])