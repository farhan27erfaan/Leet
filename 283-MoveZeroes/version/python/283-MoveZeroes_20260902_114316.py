# Last updated: 02/09/2026, 11:43:16
1class Solution(object):
2    def findMaxForm(self, strs, m, n):
3        dp = [[0] * (n + 1) for _ in range(m + 1)] 
4
5        for s in strs:
6            zero = s.count('0')
7            one = s.count('1')
8
9            for i in range(m, zero - 1, -1):
10                for j in range(n, one - 1, -1):
11                    dp[i][j] = max(dp[i][j], 1 + dp[i - zero][j - one])
12        
13        return dp[m][n]