'''
https://leetcode.com/problems/backspace-string-compare/

***test case:
"ab##"
"c#d#"
"a##c"
"#a#c"
"a#c"
"b"
"ab#c"
"ad#c"
"bxj##tw"
"bxo#j##tw"
"isfcow#"
"isfcog#w#"
'''
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def f(s):
            rst = ''
            cnt = 0
            j = len(s) - 1 
            while(j >= 0):
                if(s[j]!= '#'):
                    if(cnt == 0):
                        rst += s[j]
                        j-=1
                    else:
                        tmp = 0
                        while(cnt >0):
                            if(s[j] == '#'):
                                tmp += 2
                            
                            j = j - 1
                            cnt -= 1
                                 
                        
                        cnt = tmp
                        
                        
                else:
                    cnt += 1
                    j -= 1
            # print(rst)
            return rst
        
        return f(S) == f(T)