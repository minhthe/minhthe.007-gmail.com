'''
https://leetcode.com/problems/largest-component-size-by-common-factor
'''
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # step 1: find prime of each number
        n = len(A)
        flag = False
        factor = [True for i in range(max(A) + 1)]
        tmp = []    
        def dic_factors(num):
            if not flag:
                
                for i in range(2, int( num **(0.5) )  + 1):
                    for j in range(i*i, num+1, i ):
                        factor[j] = False
                for i in range(2, num+1):
                    if factor[i]: tmp.append(i)
                return None
            else:
                rst ={}
                # for i in range(1, int(num**0.5)+1):
                #     if factor[i] and num%i == 0:
                #         if i >1: rst[i]= True
                #         if num//i>1 and factor[num//i]: rst[num//i]= True
                for item in tmp:
                    if item > num: return rst
                    if num % item == 0: 
                        rst[item] = True
                        if num// item > 1 : rst[num//item] = True
                
                return rst
        dic_factors(max(A))
        flag = True
            
        ls_primes = {i: None for i in range(n)}
        for i,item in enumerate(A):
            ls_primes[i] = dic_factors(item)
        # print(ls_primes)
        
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
            
        def union(pos, primes):
            if pos ==  n - 1: return
            for i in range(pos + 1, n):
                other_primes = ls_primes[i]
                for key in primes:
                    if key in other_primes:
                        pu = find(i)
                        pv = find(pos)
                        if pu == pv: break
                        if rank[pu] < rank[pv]:
                            parent[pu] = pv
                        elif rank[pu] > rank[pv]:
                            parent[pv] = pu
                        else:
                            parent[pu] = pv
                            rank[pu]+=1
                            
                            
                                    
        for key in ls_primes:
            primes = ls_primes[key]
            union(key, primes)
        # print(parent)
        # count the max pranent
        ans = {}
        for i in range(n):
            p = find(i)
            ans[p] = ans[p] + 1 if p in ans else 1
        return max(ans.values())