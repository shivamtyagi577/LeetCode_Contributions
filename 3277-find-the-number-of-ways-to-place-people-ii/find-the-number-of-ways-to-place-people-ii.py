class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        # Coordinate compression
        xs = sorted(set(x for x,y in points))
        ys = sorted(set(y for x,y in points))

        x_map = {x:i for i, x in enumerate(xs)}
        y_map = {y:i for i, y in enumerate(ys)}

        # create a grid and mark points

        grid = [[0] * (len(ys) + 1) for _ in range(len(xs) + 1)]

        for x,y in points:
            grid[x_map[x]+1][y_map[y]+1] += 1

        # Build 2D prefix sum
        for i in range(1, len(xs) + 1):
                    for j in range(1, len(ys) + 1):
                        grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]

        def query(x1, y1, x2, y2):
            # Returns number of points in rectangle [(x1,y1), (x2,y2)]
            return grid[x2][y2] - grid[x1-1][y2] - grid[x2][y1-1] + grid[x1-1][y1-1]

        count = 0
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                ax, ay = points[i]
                bx, by = points[j]
                if ax <= bx and ay >= by:
                    # Compressed coordinates
                    x1 = x_map[ax] + 1
                    y1 = y_map[by] + 1
                    x2 = x_map[bx] + 1
                    y2 = y_map[ay] + 1
                    total_inside = query(x1, y1, x2, y2)
                    if total_inside == 2:  # Only Alice and Bob
                        count += 1
        return count
