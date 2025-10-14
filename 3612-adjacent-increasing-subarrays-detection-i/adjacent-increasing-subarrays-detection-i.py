class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # Helper function to check if a subarray is stricly increasing
        def isStrictlyIncreasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i+1]:
                    return False
            return True

        # Slide a window of size 2k across the array
        for i in range(len(nums) - 2*k + 1):
            if isStrictlyIncreasing(i) and isStrictlyIncreasing(i+k):
                return True
        return False