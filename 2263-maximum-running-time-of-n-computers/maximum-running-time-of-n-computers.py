class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low, high = 1, sum(batteries) // n

        def can_run(t):
            total = 0
            for b in batteries:
                total += min(b,t)
            return total >= t*n

        while low < high:
            mid = (low+high+1) // 2
            if can_run(mid):
                low = mid
            else:
                high = mid - 1

        return low