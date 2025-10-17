class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        """
        Calculates the maximum number of partitions after changing at most one character in the string.
        A partition is defined as the longest prefix with at most k distinct characters.

        Parameters:
        - s (str): Input string consisting of lowercase English letters.
        - k (int): Maximum number of distinct characters allowed in each partition.

        Returns:
        - int: Maximum number of partitions achievable.
        """
        n = len(s)

        # Initialize prefix and suffix arrays to store:
        # [0] = number of partitions
        # [1] = bitmask of characters in current segment
        # [2] = count of distinct characters in current segment
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]

        # Build prefix partition info from left to right
        num, mask, count = 0, 0, 0
        for i in range(n - 1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            left[i + 1][0] = num
            left[i + 1][1] = mask
            left[i + 1][2] = count
        # Build suffix partition info from right to left
        num, mask, count = 0, 0, 0
        for i in range(n - 1, 0, -1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            right[i - 1][0] = num
            right[i - 1][1] = mask
            right[i - 1][2] = count

        max_val = 0

        # Try changing each character and compute the resulting partitions
        for i in range(n):
            # Base segments from left and right + 2 (for the two segments around the change)
            seg = left[i][0] + right[i][0] + 2

            # Combine character masks from left and right
            tot_mask = left[i][1] | right[i][1]
            tot_count = bin(tot_mask).count("1")

            # Adjust segment count based on character change impact
            if left[i][2] == k and right[i][2] == k and tot_count < 26:
                seg += 1  # Adding a new character creates a new segment
            elif min(tot_count + 1, 26) <= k:
                seg -= 1  # Adding a character doesn't exceed k, so one segment merges

            max_val = max(max_val, seg)

        return max_val
