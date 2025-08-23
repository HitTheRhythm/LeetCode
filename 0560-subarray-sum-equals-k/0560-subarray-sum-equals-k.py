class Solution:
    def subarraySum(self, nums, k):
        count = 0
        mp = defaultdict(int)
        mp[0] = 1
        s = 0
        for num in nums:
            s += num
            if s - k in mp:
                count += mp[s - k]
            mp[s] += 1

        return count
        