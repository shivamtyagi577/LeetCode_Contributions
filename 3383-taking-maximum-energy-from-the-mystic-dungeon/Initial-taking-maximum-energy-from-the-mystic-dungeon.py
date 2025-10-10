def max_energy_gain(energy, k):
    n = len(energy)
    max_energy = float('-inf')  # Start with the lowest possible value

    for start in range(n):
        total = 0
        i = start
        while i < n:
            total += energy[i]
            i += k
        max_energy = max(max_energy, total)

    return max_energy

# Example usage:
print(max_energy_gain([5, 2, -10, -5, 1], 3))  # Output: 3
print(max_energy_gain([-2, -3, -1], 2))        # Output: -1
