class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        memo = {}
        def f(n,s,step):
            if (step, s) in memo:
                return memo[(step, s)]
            
            if s == 0:
                return 1
            rst = 0 
            for i in range(step, n):
                if s >= coins[i]:
                    rst += f( n, s - coins[i], i )
            memo[(step, s)] = rst
            return rst
        return f(n,amount, 0 )