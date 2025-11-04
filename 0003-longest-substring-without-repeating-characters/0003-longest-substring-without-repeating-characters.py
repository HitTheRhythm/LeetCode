class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0 , 0 
        window = Counter()
        ans = 0

        while right < len(s):
            window[s[right]] += 1
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            ans = max(right - left + 1,ans)
            right += 1
            
        return ans



        