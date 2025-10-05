class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            visited = [[False] * n for _ in range(m)]
            q = deque(starts)
            for r, c in starts:
                visited[r][c] = True

            for_r = range  # minor micro-optimizations aside, clarity first
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and 0 <= nc < n and
                        not visited[nr][nc] and
                        heights[nr][nc] >= heights[r][c]    # reverse flow: climb up or stay equal
                    ):
                        visited[nr][nc] = True
                        q.append((nr, nc))
            return visited

        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)

        return [[r, c] for r in range(m) for c in range(n) if pac[r][c] and atl[r][c]]

            