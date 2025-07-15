class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = nums[::-1]
        n = len(nums)
        ans = [-1] * n

        for i in range(n -1 , -1 , -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        return ans