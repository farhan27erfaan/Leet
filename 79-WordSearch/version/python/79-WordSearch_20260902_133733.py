# Last updated: 02/09/2026, 13:37:33
1class Solution(object):
2    def longestPalindromeSubseq(self, s):
3        n = len(s)
4        dp = [[0] * n for _ in range(n)]
5        for i in range(n - 1, -1, -1):
6            dp[i][i] = 1
7            for j in range(i + 1, n):
8                if s[i] == s[j]:
9                    dp[i][j] = dp[i + 1][j - 1] + 2
10                else:
11                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
12        return dp[0][n - 1]