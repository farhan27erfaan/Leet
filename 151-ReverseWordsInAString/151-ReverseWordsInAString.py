# Last updated: 11/08/2026, 11:41:53
class Solution(object):
    def reverseWords(self, s):
     words=s.split()
     result=""
     for word in words[::-1]:
        result+=word+" "
     return result.strip()

