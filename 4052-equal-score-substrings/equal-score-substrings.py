class Solution:
    def scoreBalance(self, s: str) -> bool:
        scores = [ord(c) - ord('a') + 1 for c in s]
        total = sum(scores)
        left_score = 0

        for i in range(len(s) - 1): # split point is between i and i+1
            left_score += scores[i]
            right_score = total - left_score
            if left_score == right_score:
                return True
        return False