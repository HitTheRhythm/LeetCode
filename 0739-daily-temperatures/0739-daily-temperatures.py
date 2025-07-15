class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        stack = []
        ans = [0] * n
        stack.append(0)
        for i in range(1, n):
            while stack and t[i] > t[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans

        
