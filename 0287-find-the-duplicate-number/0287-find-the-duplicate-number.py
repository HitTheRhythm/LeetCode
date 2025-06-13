class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for item, c in count.items():
            if c > 1:
                return item