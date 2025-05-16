class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = self.square)
        return points[:k]
    def square(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2