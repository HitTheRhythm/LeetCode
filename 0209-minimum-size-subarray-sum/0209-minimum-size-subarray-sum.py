class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        summ = 0
        left = 0

        for right in range(len(nums)):
            summ += nums[right]

            while summ >= target:
                curWindowLen = right - left + 1
                minLen = min(minLen, curWindowLen)
                summ -= nums[left]
                left += 1
        return 0 if minLen == float('inf') else minLen