# Last updated: 02/09/2026, 10:31:02
1class Solution:
2    def commonChars(self, words):
3        min_freq = Counter(words[0])
4        for word in words:
5            min_freq &= Counter(word)
6        return list(min_freq.elements())