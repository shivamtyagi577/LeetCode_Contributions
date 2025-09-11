class Solution(object):
    def sortVowels(self, s):   
        vowels = set("aeiouAEIOU")
        # Extract vowels from the string
        vowel_chars = [c for c in s if c in vowels]
        # Sort vowels by ASCII value
        vowel_chars.sort()
        
        # Reconstruct the string
        result = []
        vowel_index = 0
        for c in s:
            if c in vowels:
                result.append(vowel_chars[vowel_index])
                vowel_index += 1
            else:
                result.append(c)
        
        return ''.join(result)
