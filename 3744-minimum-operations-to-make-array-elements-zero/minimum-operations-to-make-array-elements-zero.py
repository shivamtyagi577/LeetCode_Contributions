class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        
        def steps_to_zero(x: int) -> int:
            """
            Efficiently compute the number of steps to reduce x to 0
            using floor(x / 4) repeatedly.
            This is equivalent to how many times we can divide x by 4
            before it becomes 0.
            """
            steps = 0
            while x > 0:
                x //= 4
                steps += 1
            return steps

        total_operations = 0

        for l, r in queries:
            # Count how many numbers require each step count
            # Instead of iterating over each number, we group by step count
            step_freq = {}
            x = l
            while x <= r:
                steps = steps_to_zero(x)
                # Find the range of numbers that share the same step count
                low = x
                high = min(r, (4 ** steps) - 1)
                count = high - low + 1
                step_freq[steps] = step_freq.get(steps, 0) + count
                x = high + 1

            # Total steps = sum of (steps * frequency)
            total_steps = sum(k * v for k, v in step_freq.items())

            # Each operation reduces two numbers, so divide by 2 (round up)
            total_operations += (total_steps + 1) // 2

        return total_operations
