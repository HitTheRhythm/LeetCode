class Solution:
    def subarraySum(self, nums, k):
        count = 0
        s = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        for num in nums:
            s += num
            if (s - k) in prefix_sum:
                count += prefix_sum[s - k]
            prefix_sum[s] += 1

        return count
        