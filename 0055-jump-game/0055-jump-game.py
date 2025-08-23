class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cover = 0

        for i in range(n - 1 ):
            cover = max(cover, i + nums[i])
            if cover <= i:
                return False
        return cover >= n - 1