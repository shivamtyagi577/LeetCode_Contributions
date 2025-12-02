class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        y_groups = defaultdict(int)
        
        for x,y in points:
            y_groups[y] += 1

        counts =list(y_groups.values())
        combs = [comb(c,2) for c in counts]

        total = 0
        prefix_sum = 0
        for c in combs:
            total = (total + prefix_sum * c) % MOD
            prefix_sum = (prefix_sum + c) % MOD

        return total