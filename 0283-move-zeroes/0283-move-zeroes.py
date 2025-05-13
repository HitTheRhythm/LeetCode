class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastF = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastF], nums[i] = nums[i], nums[lastF]
                lastF += 1
        