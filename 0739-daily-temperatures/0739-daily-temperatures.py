class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        stack = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            tem = t[i]
            while stack and tem >= t[stack[-1]]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
