class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1 : return 0
        maxProfit = 0
        b, s = 0, 1
        while s < len(prices) :
            profit = prices[s] - prices[b]
            if profit < 0 :
                b += 1
            else :
                maxProfit = max(maxProfit, profit)
                s += 1
        return maxProfit