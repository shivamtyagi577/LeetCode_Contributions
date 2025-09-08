class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def check(x):
            return '0' not in str(x)

        for i in range(1, n):
            j = n - i
            if check(i) and check(j):
                return [i, j]
