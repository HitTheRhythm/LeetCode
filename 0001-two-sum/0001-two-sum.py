class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in mp:
                mp[nums[i]] = i
            else:
                return [i, mp[comp]]
            
        