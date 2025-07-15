class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mp = {}

        for num in nums2:
            while stack and num > stack[-1]:
                mp[stack.pop()] = num
            stack.append(num)
        return [mp.get(i,-1) for i in nums1]


        



        

        
