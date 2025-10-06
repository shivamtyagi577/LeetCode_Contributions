class Solution(object):
    def swimInWater(self, grid):
        n = len(grid) # [[], [], [], [], []] -> 5

        # Helper function to check if we can reach (n-1, n-1) at time t
        def canReach(t):
            # Create a visited matrix to track visited cells
            visited = [[False]*n for _ in range(n)]

            # Using BFS starting from (0,0)
            queue = deque([(0,0)])
            visited[0][0] = True # Start with a tuple (x, y)

            while queue:
                x,y = queue.popleft() # Unpack the tuple
                # If we've reached the bottom-right cell, return True
                if x == n-1 and y == n-1:
                    return True
                
                # Explore 4-directional neighbours
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0,1)]:
                    nx, ny = x+dx, y+dy
                    # Check bounds and if the cell is not visited and elevation <= t                    
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= t:
                        visited[nx][ny] = True
                        queue.append((nx, ny)) # Add the tuple to the queue
            
            # If we exhaust all options and don't reach (n-1, n-1), return False
            return False

        # Binary search for the minimum time t
        left, right = grid[0][0], n*n -1
        while left < right:
            mid = (left + right) // 2

            # If we can reach the destination at time mid, try a smaller time
            if canReach(mid):
                right = mid
            else:
                #Otherwise, we need more time
                left = mid + 1

        # Final answer is the minimum time when path becomes possible
        return left
