class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Add all boundary cells to the heap and mark them as visited
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        trapped_water = 0
        max_height = 0

        while heap:
            height, x, y = heapq.heappop(heap)
            max_height = max(max_height, height)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    neighbor_height = heightMap[nx][ny]
                    trapped_water += max(0, max_height - neighbor_height)
                    heapq.heappush(heap, (neighbor_height, nx, ny))

        return trapped_water

            