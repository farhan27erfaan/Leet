# Last updated: 02/09/2026, 14:26:01
1class Solution:
2    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
3        corners = set()
4        area = 0
5
6        min_x = float("inf")
7        min_y = float("inf")
8        max_x = float("-inf")
9        max_y = float("-inf")
10
11        for x1, y1, x2, y2 in rectangles:
12
13            area += (x2 - x1) * (y2 - y1)
14
15            min_x = min(min_x, x1)
16            min_y = min(min_y, y1)
17            max_x = max(max_x, x2)
18            max_y = max(max_y, y2)
19
20            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
21                if point in corners:
22                    corners.remove(point)
23                else:
24                    corners.add(point)
25
26        expected_area = (max_x - min_x) * (max_y - min_y)
27
28        if area != expected_area:
29            return False
30
31        expected_corners = {
32            (min_x, min_y),
33            (min_x, max_y),
34            (max_x, min_y),
35            (max_x, max_y)
36        }
37
38        return corners == expected_corners