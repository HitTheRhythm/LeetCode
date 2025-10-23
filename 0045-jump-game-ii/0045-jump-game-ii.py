class Solution:
    def jump(self, nums: List[int]) -> int:
        i = j = 0
        cur = cmax = res = 0

        for i in range(len(nums) - 1):
            cmax = max(cmax, i + nums[i])
            if i == cur:
                res += 1
                cur = cmax
        return res