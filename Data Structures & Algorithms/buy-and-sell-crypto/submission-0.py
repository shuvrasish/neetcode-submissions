class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        maxr = prices[n - 1]
        maxProfit = 0

        for i in range(n - 2, -1, -1):
            if prices[i] < maxr:
                maxProfit = max(maxProfit, maxr - prices[i])
            else:
                maxr = prices[i]
        
        return maxProfit

