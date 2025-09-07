class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = nums.count(val)
        print(x)
        for i in range(x):
            nums.remove(val)
        return len(nums)
        