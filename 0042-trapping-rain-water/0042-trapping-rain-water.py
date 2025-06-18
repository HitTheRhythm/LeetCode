class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        i, j = 0 , len(height) - 1
        pre = 0
        suf = 0
        while i <= j:
            pre = max(pre, height[i])
            suf = max(suf, height[j])
            if pre < suf:
                ans += pre - height[i]
                i += 1
            else:
                ans += suf - height[j]
                j -= 1
        return ans