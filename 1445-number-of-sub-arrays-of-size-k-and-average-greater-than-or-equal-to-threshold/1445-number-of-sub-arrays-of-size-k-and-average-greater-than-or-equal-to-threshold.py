class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        cur = sum(arr[:k])
        if cur / k >= threshold: 
            count += 1
        for i in range(k, len(arr)):
            cur += arr[i] - arr[i - k]
            if cur / k >= threshold:
                count += 1
        return count
            
        