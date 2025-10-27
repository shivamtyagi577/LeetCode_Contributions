class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Step 1: Count the number of devices in each row
        device_counts = [row.count('1') for row in bank if row.count('1') > 0]

        # Step 2: Calculate beams between consecutive non-empty rows
        total_beams = 0
        for i in range(1, len(device_counts)):
            total_beams += device_counts[i - 1] * device_counts[i]

        return total_beams
