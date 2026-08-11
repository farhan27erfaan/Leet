# Last updated: 11/08/2026, 11:40:09
"""
class Solution(object):
    def numberOfSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            temp = set()
            for j in range(i, len(s)):
                temp.add(s[j])
                if len(temp) == 3:
                    count += 1
        return count
"""
class Solution(object):
    def numberOfSubstrings(self, s):

        left = 0
        count = 0

        freq = {
            'a': 0,
            'b': 0,
            'c': 0
        }

        n = len(s)

        for right in range(n):

            freq[s[right]] += 1

            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:

                count += n - right

                freq[s[left]] -= 1
                left += 1

        return count
                

        