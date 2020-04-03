'''
***time complexity: O(n*m)
'''
if __name__ == '__main__':
    s = 'abdfdsfavcvfabdc'
    p = 'abc'
    def f(s, p):
        i, j , pos = 0,0,0
        while(i<len(s)):
            pos = i
            while(j<len(p) and pos < len(s)):
                if(s[pos] != p[j]):
                    i+=1
                    j = 0
                    break
                else:
                    if(j == len(p) -1): return True
                    j += 1 
                    pos += 1
        return False                    
                
    ans = f(s, p)
    print(ans)