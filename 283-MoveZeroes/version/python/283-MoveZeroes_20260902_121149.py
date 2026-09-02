# Last updated: 02/09/2026, 12:11:49
1class Solution(object):
2    def removeComments(self, source):
3        ans, inComment = [], False
4        new_str = ""
5        for c in source:
6            if not inComment: new_str = ""
7            i, n = 0, len(c)
8           
9            while i < n:
10                if inComment:
11                    if c[i:i + 2] == '*/' and i + 1 < n:
12                        i += 2
13                        inComment = False
14                        continue
15                    i += 1
16
17                else:
18                    if c[i:i + 2] == '/*' and i + 1 < n:
19                        i += 2
20                        inComment = True
21                        continue
22                    if c[i:i + 2] == '//' and i + 1 < n:
23                        break
24                    new_str += c[i]
25                    i += 1
26            if new_str and not inComment:
27                ans.append(new_str)
28                    
29
30        return ans
31        