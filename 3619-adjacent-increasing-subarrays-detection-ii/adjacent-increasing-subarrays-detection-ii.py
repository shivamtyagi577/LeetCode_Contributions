class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        # No place to put two adjacent, but per constraints n >= 2.
        if n < 2:
            return 0

        # inc_start[i]: length of strictly increasing run starting at i
        inc_start = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                inc_start[i] = inc_start[i+1] + 1
            else:
                inc_start[i] = 1

        ans = 0
        cur_end = 1 # Length of strictly increasing run ending at i
        for i in range(n-1):
            if i > 0:
                if nums[i-1] < nums[i]:
                    cur_end += 1
                else:
                    cur_end = 1
            # boundary between i and i+1
            ans = max(ans, min(cur_end, inc_start[i+1]))
        return ans        