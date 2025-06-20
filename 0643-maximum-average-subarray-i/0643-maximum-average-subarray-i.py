class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = 0
        for i in range(k):
            cur += nums[i]
        ans = cur
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i - k]
            ans = max(ans,cur)
        return ans / k