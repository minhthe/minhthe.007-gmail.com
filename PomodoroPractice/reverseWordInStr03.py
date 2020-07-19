'''
https://leetcode.com/problems/reverse-words-in-a-string
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        ss = list(item for item in s.split(" ") if len(item)>0)
        i, j= 0 , len(ss)-1
        while(i < j):
            ss[i], ss[j] = ss[j],ss[i]
            i+=1
            j-=1
        return ' '.join(ss)