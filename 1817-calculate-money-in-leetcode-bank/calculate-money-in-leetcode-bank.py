class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total = 0

        # Full weeks
        for i in range(weeks):
            total += (7 * (i + 1)) + (6 * 7) // 2  # Arithmetic sum: a + (a+1) + ... + (a+6)

        # Remaining days
        for i in range(days):
            total += weeks + 1 + i

        return total
