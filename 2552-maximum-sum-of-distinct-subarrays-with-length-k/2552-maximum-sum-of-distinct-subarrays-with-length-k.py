class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = cur = 0
        hset = set()
        i = j = 0
        while j < len(nums):
            while len(hset) == k or nums[j] in hset:
                hset.remove(nums[i])
                cur -= nums[i]
                i += 1
            hset.add(nums[j])
            cur += nums[j]
            j += 1
            if len(hset) == k:
                ans = max(ans, cur)
        return ans
            
        return ans
