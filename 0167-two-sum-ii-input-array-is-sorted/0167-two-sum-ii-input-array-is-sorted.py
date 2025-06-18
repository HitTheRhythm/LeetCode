class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while True:
            s = nums[left] + nums[right]
            if s == target:
                break
            elif s > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]