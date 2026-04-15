class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        n = min(len(word1), len(word2))
        for i in range(n) :
            s += word1[i] + word2[i]
        if i+1 < len(word1) :
            s += word1[i+1:]
        else :
            s += word2[i+1:]
        return s

