class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0 ,0
        product = 1
        ans = 0

        while right < len(nums):
            product *= nums[right]
            right += 1
            while product >= k and left < right:
                product //= nums[left]
                left +=1
            ans += right - left
        return ans
            
