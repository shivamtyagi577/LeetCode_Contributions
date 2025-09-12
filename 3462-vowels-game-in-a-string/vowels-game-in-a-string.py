class Solution(object):
    def doesAliceWin(self, s):
        vowels = set("aeiou")
        prefix_parity = {0: 1}  # parity 0 seen once (empty prefix)
        count = 0
        for c in s:
            if c in vowels:
                count += 1
            parity = count % 2
            if parity == 1 and prefix_parity.get(0, 0) > 0:
                return True  # Found a substring with odd number of vowels
            prefix_parity[parity] = prefix_parity.get(parity, 0) + 1
        return False
