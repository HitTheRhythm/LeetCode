class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = inf

        for i in range(len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            if prices[i] - minp > maxp:
                maxp = prices[i] - minp
        return maxp