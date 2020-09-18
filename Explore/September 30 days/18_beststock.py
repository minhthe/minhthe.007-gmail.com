class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_running = int(1e9)
        max_profit = 0 
        for i in range(1, len(prices)):
            min_running = min(min_running, prices[i-1])
            max_profit = max(max_profit, prices[i] - min_running)
        return max_profit