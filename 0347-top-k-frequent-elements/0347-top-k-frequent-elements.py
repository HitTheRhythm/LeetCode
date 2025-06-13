class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1
        sorted_mp = sorted(mp.items(), key = lambda item: item[1], reverse = True)
        res = []

        for i in range(k):
            res.append(sorted_mp[i][0])
        return res