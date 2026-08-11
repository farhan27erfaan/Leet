# Last updated: 11/08/2026, 11:42:38
class Solution:
    def lengthOfLastWord(self, s):
        words=s.split()
        for word in words[::-1]:
            size=len(word)
            break
        return size
