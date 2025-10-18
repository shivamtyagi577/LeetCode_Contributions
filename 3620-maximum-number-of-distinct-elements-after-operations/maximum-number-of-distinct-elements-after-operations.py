class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        # Build intervals [L, R]
        intervals = [(x - k, x + k) for x in nums]
        intervals.sort(key=lambda p: p[1])  # sort by R ascending

        cur = -10**20  # sufficiently small sentinel; could also use float('-inf') with care
        distinct = 0

        for L, R in intervals:
            if cur < L:
                cur = L  # move cur up to interval start
            if cur <= R:
                # assign 'cur' to this interval
                distinct += 1
                cur += 1  # next assignment must be a different integer

        return distinct
