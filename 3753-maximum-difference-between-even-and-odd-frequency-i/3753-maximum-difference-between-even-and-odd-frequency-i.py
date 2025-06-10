class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd = []
        even = [] 
        for count in freq.values():
            if count % 2 == 1:
                odd.append(count)
            elif count > 0:
                even.append(count)
        if not odd or not even:
            return 0
        
        return max(odd) - min(even)