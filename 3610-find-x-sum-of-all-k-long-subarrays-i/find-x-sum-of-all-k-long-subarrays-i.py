class Solution(object):
    def findXSum(self, nums, k, x):
        n = len(nums)
        result = []

        for i in range(n-k+1):
            subarray = nums[i:i+k]
            freq = Counter(subarray)

            # Sort by frequency descending, then by value descending
            sorted_items = sorted(freq.items(), key= lambda item:(-item[1], -item[0]))

            # get the top x frequesnt elements
            top_x_element = set(item[0] for item in sorted_items[:x])

            #Sum only the elements in top_x_elements
            x_sum = sum(num for num in subarray if num in top_x_element)
            result.append(x_sum)

        return result