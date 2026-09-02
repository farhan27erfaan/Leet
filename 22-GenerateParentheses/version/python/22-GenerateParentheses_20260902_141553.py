# Last updated: 02/09/2026, 14:15:53
1from typing import List
2
3class Solution:
4    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
5
6        rows, cols = len(dungeon), len(dungeon[0])
7
8        dp = [[0] * cols for _ in range(rows)]
9        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
10
11        for i in range(rows - 2, -1, -1):
12            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])
13
14        for j in range(cols - 2, -1, -1):
15            dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])
16
17        for i in range(rows - 2, -1, -1):
18            for j in range(cols - 2, -1, -1):
19                min_health_needed = min(dp[i + 1][j], dp[i][j + 1])
20                dp[i][j] = max(1, min_health_needed - dungeon[i][j])
21        return dp[0][0]