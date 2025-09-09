class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        # Using MOD to keep the result within bound(as the number can be very high)
        MOD = 10**9 + 7

        # dp[i] = number of people who learn the secret on day i
        dp = [0] * (n+1) # [0, 0, 0, 0, 0, 0, 0]
        dp[1] = 1        # On day 1, one person knows the secret
        share = 0        # Number of people who can share the secret
        
        # A person cannot share the secret on the same day they forgot it, or on any day afterwards.
        for day in range(2, n+1):
            # People who can start sharing today
            if day - delay >= 1:
                share += dp[day - delay]
            # People who forget the secret today
            if day - forget >= 1:
                share -= dp[day - forget]

            # Number of people who learn the secret today
            dp[day] = share % MOD

        # Total people who still know the secret on day n
        total = 0
        for day in range(n -  forget + 1, n + 1):
            total += dp[day]
            
        return total % MOD
