class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()

        # --- Part 1: existing targets v ---
        ans = 0
        L = 0
        R = -1
        i = 0
        while i < n:
            v = nums[i]
            # Find run [i, j) where nums[i:j] == v
            j = i
            while j < n and nums[j] == v:
                j += 1
            run_len = j - i  # freq(v)

            low, high = v - k, v + k

            # Move L to first index with nums[L] >= low
            while L < n and nums[L] < low:
                L += 1
            # Move R to last index with nums[R] <= high
            while R + 1 < n and nums[R + 1] <= high:
                R += 1

            covering = max(0, R - L + 1)  # # elements that can become v (including those already equal)
            cand_existing = min(covering, run_len + numOperations)
            if cand_existing > ans:
                ans = cand_existing

            i = j  # next distinct value

        # --- Part 2: non-existing targets via max overlap M ---
        # Build sweep events on integer line with inclusive ranges [x - k, x + k]
        events = {}
        for x in nums:
            L = x - k
            R = x + k
            events[L] = events.get(L, 0) + 1
            # Use R + 1 with -1 to model inclusive range on integers
            events[R + 1] = events.get(R + 1, 0) - 1

        curr = 0
        M = 0
        for pos in sorted(events):
            curr += events[pos]
            if curr > M:
                M = curr

        cand_new = min(M, numOperations)
        ans = max(ans, cand_new)

        return ans
