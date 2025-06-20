class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # 修正：比较 nums[mid] 和 nums[right]
            if nums[mid] > nums[right]:
                # 最小值在右半部分
                left = mid + 1
            else:
                # 最小值在左半部分（包括mid）
                right = mid
        
        return nums[left]