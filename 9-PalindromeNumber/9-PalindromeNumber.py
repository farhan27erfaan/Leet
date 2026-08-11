# Last updated: 11/08/2026, 11:43:19
class Solution(object):
    def isPalindrome(self, x):
        f = str(x)
        return f == f[::-1]
 