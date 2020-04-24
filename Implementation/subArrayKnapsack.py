if __name__ == '__main__':
    
    a = [1,2,3,4]
    tmp, rst = [],[]
    p = -1
    
    def f(tmp, rst, a, p):
        
        
        if p == len(a):
            rst.append(tmp[:])
            return 
        
        if 0<= p < (len(a)): 
            tmp.append(a[p])
        f(tmp, rst, a, p+1)
        if len(tmp): 
            tmp.pop()
        else:                     #### when run the end of the loop -> if not it will run exactly duplication values
            return rst
        f(tmp, rst, a, p+1)
        return rst
          
    f(tmp, rst, a, p)
    print(rst)
    print(len(rst))