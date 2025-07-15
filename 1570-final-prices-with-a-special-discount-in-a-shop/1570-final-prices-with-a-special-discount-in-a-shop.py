class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = prices[:]
        stack = []
        for i in range(n):
            price = prices[i]
            while stack and prices[stack[-1]]>= price:
                ans[stack[-1]] -= price
                stack.pop()
            
            stack.append(i)
        return ans