class Solution:
    def countPartitions(self, nums: List[int]) -> int:        
        total_sum = sum(nums)
        n = len(nums)
        
        if total_sum % 2 == 0:
            return n - 1  # all partitions valid
    
        return 0
