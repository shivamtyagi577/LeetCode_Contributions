class Solution(object):
    def maxFreqSum(self, s):
       vowels = set("aeiou")
       freq = Counter(s)

       vowel_freqs = [freq[ch] for ch in vowels if ch in freq]
       consonant_freqs = [freq[ch] for ch in freq if ch not in vowels]

       max_vowel_freq = max(vowel_freqs) if vowel_freqs else 0
       max_consonant_freq = max(consonant_freqs) if consonant_freqs else 0

       return max_vowel_freq + max_consonant_freq


        