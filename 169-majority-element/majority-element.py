class Solution(object):
    def majorityElement(self, nums):
        majority = None
        count = 0

        for num in nums:
            if count == 0:
                majority = num
            count+= (1 if num == majority else -1)

        return majority
        