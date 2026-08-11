# Last updated: 11/08/2026, 11:40:58
class Solution(object):
    def isAnagram(self, s, t):

        a = "".join(sorted(s))
        b = "".join(sorted(t))

        if a == b:
            return True
        else:
            return False
        