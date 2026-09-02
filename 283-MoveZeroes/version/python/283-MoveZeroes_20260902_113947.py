# Last updated: 02/09/2026, 11:39:47
1class Solution:
2    def minimumTotal(self, triangle):
3        n = len(triangle)
4        for i in range(n - 2, -1, -1):
5            for j in range(i + 1):
6                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
7        return triangle[0][0]