# Last updated: 02/09/2026, 10:02:02
1class Solution(object):
2    def findWords(self, words):
3        m = {}
4        for c in "qwertyuiop":
5            m[c] = 1
6        for c in "asdfghjkl":
7            m[c] = 2
8        for c in "zxcvbnm":
9            m[c] = 3
10        ans = []
11        for w in words:
12            lw = w.lower()
13            r = m[lw[0]]
14            if all(m[ch] == r for ch in lw):
15                ans.append(w)
16        return ans