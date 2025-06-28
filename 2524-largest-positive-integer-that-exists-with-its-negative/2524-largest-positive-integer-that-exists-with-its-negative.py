class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mp = {}
        res = - 1

        for i in range(len(nums)):
            comp = 0  - nums[i]
            if comp not in mp:
                mp[nums[i]] = 1
            else:
                res = max(res, abs(nums[i]))

        return res
        