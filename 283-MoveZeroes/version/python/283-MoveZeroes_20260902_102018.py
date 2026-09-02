# Last updated: 02/09/2026, 10:20:18
1class Solution(object):
2    def nextGreatestLetter(self, letters, target):
3        for letter in letters:
4            if letter>target:
5                return letter
6        return letters[0]
7        