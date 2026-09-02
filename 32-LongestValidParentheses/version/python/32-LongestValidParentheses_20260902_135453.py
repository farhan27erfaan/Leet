# Last updated: 02/09/2026, 13:54:53
1class Solution:
2    def longestValidParentheses(self, s):
3
4        stack = [-1]
5        maxLength = 0
6
7        for i, ch in enumerate(s):
8
9            if ch == '(':
10
11                stack.append(i)
12
13            else:
14
15                stack.pop()
16
17                if not stack:
18
19                    stack.append(i)
20
21                else:
22
23                    maxLength = max(maxLength, i - stack[-1])
24
25        return maxLength