class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        def normalize_dir(dx: int, dy: int) -> Tuple[int,int]:
            """
            Reduce (dx,dy) to a canonical direction vector that represents slope.
            Ensures uniqueness : dx > 0, or dx == 0 and dy == 0.
            """
            if dx == 0 and dy == 0:
                return (0,0)
            g = gcd(dx,dy)
            dx //= g
            dy //= g

            # fix sign to get canonical orientation
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy

            return (dx,dy)

        """
        Counts the number of unique trapezoids (convex quadrilaterals with atleast one pair of parallel sides)
        fromed by any 4 distinct points.
        Includes parallelograms, but they are corrected to be counted once.
        """
        n = len(points)
        if n < 4:
            return 0             
        
        # 1) Build sets of points on each line (by slope and offset).
        # Represent a line by (slope_dir, t), where t = dot(normal, point) with normal ⟂ slope_dir.
        lines_points = defaultdict(set)  # key: (dxn, dyn, t) -> set of point indices
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                dxn, dyn = normalize_dir(dx, dy)
                nx, ny = dyn, -dxn  # a perpendicular normal to (dxn, dyn)
                t = nx * x1 + ny * y1
                key = (dxn, dyn, t)
                lines_points[key].add(i)
                lines_points[key].add(j)

        # 2) For each slope, collect number of ways to pick a side on each parallel line: a_i = C(c_i, 2).
        slope_to_side_counts = defaultdict(list)  # slope_dir -> list of binom(c_i, 2)
        for (dxn, dyn, t), idx_set in lines_points.items():
            c = len(idx_set)
            if c >= 2:
                slope_to_side_counts[(dxn, dyn)].append(c * (c - 1) // 2)

        # 3) Count all quadrilaterals that have at least one pair of parallel sides
        # by pairing two distinct parallel lines for each slope.
        total_with_at_least_one_parallel_pair = 0
        for counts in slope_to_side_counts.values():
            if len(counts) >= 2:
                s = sum(counts)
                s2 = sum(val * val for val in counts)
                total_with_at_least_one_parallel_pair += (s * s - s2) // 2

        # 4) Count parallelograms via midpoint trick, EXCLUDING collinear pairs.
        # For each pair of points, compute doubled midpoint and segment direction.
        mid_dir_counts = defaultdict(lambda: defaultdict(int))  # mid_key -> {dir -> count}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                mid_key = (x1 + x2, y1 + y2)  # doubled midpoint (avoid fractions)
                dir_key = normalize_dir(x2 - x1, y2 - y1)
                mid_dir_counts[mid_key][dir_key] += 1

        parallelograms = 0
        for dir_count_map in mid_dir_counts.values():
            k = sum(dir_count_map.values())  # total segments with this midpoint
            if k >= 2:
                total_pairs = k * (k - 1) // 2
                collinear_pairs = sum(c * (c - 1) // 2 for c in dir_count_map.values())
                parallelograms += (total_pairs - collinear_pairs)

        # 5) Correct for double counting of parallelograms (each counted twice in step 3).
        result = total_with_at_least_one_parallel_pair - parallelograms
        # As a sanity check, result should never be negative; clamp at 0 (though with the fix it shouldn't be).
        return max(result, 0)
