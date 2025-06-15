class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        res = [-1] * n
        
        window = 0
        for i in range(k , n - k):
            if window == 0:
                window = sum(nums[0:(2 * k + 1)])
                res[i] = window // (2 * k + 1)
                continue
            window += nums[i + k] - nums[i - k -1]
            res[i] = window // (2 * k + 1)
            
        return res
