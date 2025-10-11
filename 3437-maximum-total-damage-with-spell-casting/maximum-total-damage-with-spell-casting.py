class Solution(object):
    def maximumTotalDamage(self, power):
        
        # Step 1: Count total damage for each unique spell value
        damage_counter = Counter(power)
        damage_map = {d: d * count for d, count in damage_counter.items()}
        
        # Step 2: Sort the unique damage values
        unique_damages = sorted(damage_map.keys())
        
        # Step 3: Dynamic Programming
        n = len(unique_damages)
        dp = [0] * n
        
        for i in range(n):
            current_damage = damage_map[unique_damages[i]]
            
            # Find the last index j such that unique_damages[j] < unique_damages[i] - 2
            j = i - 1
            while j >= 0 and unique_damages[i] - unique_damages[j] <= 2:
                j -= 1
            
            if j >= 0:
                dp[i] = max(dp[i-1], current_damage + dp[j])
            else:
                dp[i] = max(dp[i-1] if i > 0 else 0, current_damage)
        
        return dp[-1]