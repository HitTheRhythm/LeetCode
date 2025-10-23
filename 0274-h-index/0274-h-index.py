class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        i = 0
        while i < n and citations[n - 1 - i] > i:
            i += 1
        return i 
        
        