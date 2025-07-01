class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        ratio = {}
        ans = 0

        for x, y in rectangles:
            rat = x / y
            if rat not in ratio:
                ratio[rat] = 0
            else:
                ratio[rat] += 1
                ans += ratio[rat]
        return ans

                
                