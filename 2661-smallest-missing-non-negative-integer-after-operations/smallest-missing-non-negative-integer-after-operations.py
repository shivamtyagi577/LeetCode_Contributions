class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = [0] * value
        for num in nums:
            r = (num % value + value) % value
            freq[r] += 1
        
        x = 0
        while True:
            r = x % value
            if freq[r] > 0:
                freq[r] -= 1
                x+= 1
            else:
                return x