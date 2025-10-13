class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]

        for i in range(1, len(words)):
            # CHeck if current word is an anagram of the Last word in a result
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])

        return result