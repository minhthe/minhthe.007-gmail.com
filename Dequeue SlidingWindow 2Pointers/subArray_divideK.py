'''
https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/310767/(Python)-Concise-Explanation-and-Proof
-> good explanation
'''
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # cnt  = 0
        # n = len(A)
        # for i in range(n)    :
        #     s = A[i]
        #     if s% K ==0: cnt+=1
        #     for j in range(i+1, n):
        #         s += A[j]
        #         if s % K == 0: cnt+=1
        # return cnt
        n = len(A)
        mp = {0:1}
        s = 0
        cnt = 0
        for i,v in enumerate(A):
            s += v
            if s % K in mp:
                cnt += mp[s%K]
                mp[s%K] += 1
            else:
                mp[s%K] = 1
        return cnt
              