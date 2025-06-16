class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = cur= 0
        mp = {}
        for i in range(len(nums)):

            mp[nums[i]] = mp.get(nums[i],0) + 1
            cur += nums[i]
            if i < k - 1:
                continue 
            if len(mp) >= m:
                ans = max(cur,ans)
            mp[nums[i - k + 1]] -= 1
            if mp[nums[i - k + 1]] == 0:
                del mp[nums[i - k + 1]]
            cur -= nums[i - k + 1]

        return ans
            