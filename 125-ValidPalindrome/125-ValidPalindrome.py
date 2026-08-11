# Last updated: 11/08/2026, 11:42:02
class Solution(object):
    def isPalindrome(self, s):
        new = ""
        for i in s:
            if i.isalnum():
                new += i.lower()
        return new == new[::-1]
        