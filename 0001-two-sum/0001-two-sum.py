class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            comp = target  - nums[i]
            if comp in mapping:
                return [i , mapping[comp]]
            mapping[nums[i]] = i
        return []
        
