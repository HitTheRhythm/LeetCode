class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        ratio = {}
        ans = 0

        for i in range(len(rectangles)):
            rat = rectangles[i][0] / rectangles[i][1]
            if rat not in ratio:
                ratio[rat] = 0
            else:
                ratio[rat] += 1
                ans += ratio[rat]
        return ans

                
                