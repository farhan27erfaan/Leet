# Last updated: 02/09/2026, 11:09:28
1class Solution(object):
2    def largestTriangleArea(self, points):
3        length = len(points)
4        area = 0
5        for i in range(length):
6            for j in range(i, length):
7                for k in range (j, length):
8                    x1 = points[i][0]
9                    x2 = points[j][0]
10                    x3 = points[k][0]
11
12                    y1 = points[i][1]
13                    y2 = points[j][1]
14                    y3 = points[k][1]
15
16                    area = max(abs(0.5 * (x1*(y2-y3) + x2*(y3 - y1) + x3*(y1-y2))), area)
17        return area
18      