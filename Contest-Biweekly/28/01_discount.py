class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        rst =  []
        n = len(prices)
        for i in range(n-1):
            flag = True
            for j in range(i+1,n):
                if prices[j] <= prices[i]:
                    rst.append(prices[i] - prices[j])
                    flag = False
                    break
            if flag:
                rst.append(prices[i])
        # print(rst)
        rst.append(prices[-1])
        return rst