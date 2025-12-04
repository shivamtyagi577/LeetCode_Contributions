class Solution:
    def countCollisions(self, directions: str) -> int:
        # Convert to list only if you plan to mutate, here string slicing is enough.
        n = len(directions)
        i = 0

        #skip all leading 'L' (they move left and escape)
        while i < n and directions[i] == 'L':
            i+=1

        j = n-1
        #skip all trailing 'R' (they move right and escape)
        while j >= 0 and directions[j] == 'R':
            j -= 1

        if i > j:
            return 0

        # Count collisions : every 'L' or 'R' in the middle segment will collide.
        middle = directions[i:j+1]
        return sum(1 for c in middle if c!= 'S')