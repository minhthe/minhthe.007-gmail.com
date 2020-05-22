'''
way 1 : same find the divosors 
NOT testing all cases: 
'''
if __name__ == '__main__':
    def f(a,b):
        
        k = min(a,b)
        t = max(a,b)
        for i in range(1,int( k ** (0.5)) + 1):
            if k % i == 0:
                j = k // i 
                if t % j == 0:
                    return j
        
    a, b = 5, 7
    ans = f(a,b)
    print(ans)

    '''
    trick remember:
    1. a ,b = b , a% b
    2. divide b -> b = 0 -> return  a
    '''
if __name__ == '__main__':
    def f(a,b):
        
       
        while(b) :
           a, b = b , a % b 
        return a 
       
    a, b = 5, 7
    ans = f(a,b)
    print(ans)    