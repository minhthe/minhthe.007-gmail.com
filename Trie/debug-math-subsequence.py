'''
https://leetcode.com/problems/number-of-matching-subsequences/
'''
import collections
if __name__== '__main__':
    def numMatchingSubseq( S, words)  :
        count=0
        needed= collections.defaultdict(list)
        
        for w in words:
            needed[w[0]].append((1, w))
        # print('frst',needed)
        for c in S:
            if c in needed:
                nextUps= needed[c]
                del needed[c]
                for i,w in nextUps:
                    if i== len(w):
                        count+=1
                    else:
                        needed[w[i]].append((i+1, w))
                        # print(needed)
        return count
    
    
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    ans = numMatchingSubseq(S, words)
    print(ans)