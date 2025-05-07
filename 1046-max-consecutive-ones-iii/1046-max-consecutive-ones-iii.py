class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left= 0
        window = 0
        maxl = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                window += 1
            while right - left + 1 - window > k:
                if nums[left] == 1:
                    window -= 1
                left += 1
            maxl = max(maxl,right - left + 1)
        return maxl