class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sett = set(nums)
        print(sett)
        listt = list(sett)
        del nums[0:]
        #nums.clear()
        print(nums)
        for i in range(len(listt)):
            nums.insert(i,listt[i])
        nums.sort()