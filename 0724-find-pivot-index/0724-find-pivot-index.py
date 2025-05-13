class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i-1]+ nums[i - 1]
        for i in range(1, len(pre)):
            left = pre[i- 1] - pre[0]
            right = pre[n] - pre[i]
            if left == right:
                return i - 1
        return -1 
