class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        points.sort(key=lambda p: (p[0], -p[1])) # Sort by x ascending, y descending
        for i, (x1, y1) in enumerate(points):
            y = float('-inf') # Track the highest y2 we've used so far
            for (x2, y2) in points[i + 1:]:
                if y1 >= y2 > y:
                    count += 1
                    y = y2
        return count     