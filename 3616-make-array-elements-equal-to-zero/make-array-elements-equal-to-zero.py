class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(start, direction):
            n = len(nums)
            curr = start
            dir = direction  # +1 for right, -1 for left
            nums_copy = nums[:]

            while 0 <= curr < n:
                if nums_copy[curr] == 0:
                    curr += dir
                elif nums_copy[curr] > 0:
                    nums_copy[curr] -= 1
                    dir *= -1  # reverse direction
                    curr += dir
                else:
                    break

            return all(x == 0 for x in nums_copy)

        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if simulate(i, -1):  # try left
                    count += 1
                if simulate(i, 1):   # try right
                    count += 1

        return count
