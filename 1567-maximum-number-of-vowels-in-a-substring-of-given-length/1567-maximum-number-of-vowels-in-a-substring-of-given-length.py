class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vow = 0

        for i, ch in enumerate(s):
            if ch in "aeiou":
                vow += 1
            if i < k - 1:
                continue
            ans = max(ans,vow)
            if s[i - k + 1] in "aeiou":
                vow -= 1
        return ans