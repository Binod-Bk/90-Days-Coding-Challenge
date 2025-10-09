class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        length = 0
        merged = []
        while length < min(len(word1), len(word2)):
                merged.append(word1[length])
                merged.append(word2[length])
                length = length + 1
        merged.extend(word1[length:])
        merged.extend(word2[length:])
        return ''.join(merged)