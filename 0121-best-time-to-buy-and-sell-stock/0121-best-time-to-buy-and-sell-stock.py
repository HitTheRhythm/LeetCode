class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        min_price = inf

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > maxp:
                maxp = prices[i] - min_price
        return maxp