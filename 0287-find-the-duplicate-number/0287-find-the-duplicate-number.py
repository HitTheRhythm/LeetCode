class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return nums[slow]
            else:
                slow += 1
                fast += 1