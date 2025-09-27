class Solution:
    def triangle_area(self, points: List[List[int]]) -> float:
        # Shoelace formula for triangle area
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0.0
        # Generate all combinations of 3 points
        for combo in combinations(points, 3):
            area = self.triangle_area(combo)
            max_area = max(max_area, area)
        return max_area


