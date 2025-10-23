class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = [int(c) for c in s]
        while len(arr) > 2:
            arr = [(arr[i] + arr[i+1]) % 10 for i in range(len(arr) - 1)]
        return arr[0] == arr[1]
