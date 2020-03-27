'''
https://leetcode.com/problems/sort-integers-by-the-power-value/
'''
class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        ans = {}
        mp = {}
        def cnt_step(num, mp):
            if(num == 1):
                mp[num] = 0
                return 0
            if(num in mp):
                return mp[num]
            else:
                if(num&1):
                    return 1 + cnt_step(num*3+1, mp)
                else:
                    return 1+ cnt_step(num/2, mp)
        for num in range(lo, hi+1):
            if(num in mp):
                tmp = mp[num]
            else:
                tmp = cnt_step(num, mp)
                mp[num] = tmp
            ans[num] =  ( (tmp , num)  )
        # print(ans)
        return sorted(ans.items(), key = lambda x: x[1])[k-1][0]
        