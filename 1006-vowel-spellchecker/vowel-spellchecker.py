class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def normalize_vowels(word):
            vowels = set('aeiou')
            return ''.join('*' if c in vowels else c for c in word.lower())

        exact_words = set(wordlist)
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            lower = word.lower()
            vowel_norm = normalize_vowels(word)
            if lower not in case_map:
                case_map[lower] = word
            if vowel_norm not in vowel_map:
                vowel_map[vowel_norm] = word

        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            elif query.lower() in case_map:
                result.append(case_map[query.lower()])
            elif normalize_vowels(query) in vowel_map:
                result.append(vowel_map[normalize_vowels(query)])
            else:
                result.append("")
        return result
