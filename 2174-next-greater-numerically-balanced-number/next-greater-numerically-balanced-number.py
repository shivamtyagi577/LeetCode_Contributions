class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_numerically_balanced(x):
            digits = list(str(x))
            digit_counter = Counter(digits)
            for digit, count in digit_counter.items():
                if int(digit) != count:
                    return False
            return True

        current = n+1
        while True:
            if is_numerically_balanced(current):
                return current
            current += 1