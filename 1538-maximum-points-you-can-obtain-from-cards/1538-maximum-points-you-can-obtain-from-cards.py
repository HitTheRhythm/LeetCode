class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        suml = sum(c[:k])
        sumr = 0
        ans = suml
        for i in range(k):
            suml -= c[k - i - 1]
            sumr += c[len(c) - 1 - i]
            ans = max(suml + sumr, ans)
        return ans