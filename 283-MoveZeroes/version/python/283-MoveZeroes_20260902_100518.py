# Last updated: 02/09/2026, 10:05:18
1class Solution:
2
3    def findRelativeRanks(self, score: List[int]) -> List[str]:
4        score = [(n, i) for i, n in enumerate(score)]
5        score.sort(key=lambda x: x[0], reverse=True)
6
7        op = [0] * len(score)
8
9        for i in range(len(score)):
10            if i == 0:
11                op[score[i][1]] = 'Gold Medal'
12            elif i == 1:
13                op[score[i][1]] = 'Silver Medal'
14            elif i == 2:
15                op[score[i][1]] = 'Bronze Medal'
16            else:
17                op[score[i][1]] = f'{i + 1}'
18
19        return op