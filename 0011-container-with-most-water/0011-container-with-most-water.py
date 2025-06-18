class Solution:
    def maxArea(self, h: List[int]) -> int:
        i, j = 0, len(h) -1 
        res = float('-inf')

        while i < j:
            area = min(h[i], h[j]) * (j - i)
            res = max(res, area)
            if h[i]< h[j]:
                i += 1
            else:
                j -= 1
        return res