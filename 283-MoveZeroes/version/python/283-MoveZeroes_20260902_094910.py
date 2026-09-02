# Last updated: 02/09/2026, 09:49:10
1class Solution(object):
2    def summaryRanges(self, nums):
3        res = []
4        if not nums:
5            return res
6        start = nums[0]
7        end = nums[0]
8        for n in nums[1:]:
9            if n == end + 1:
10                end = n
11            else:
12                if start == end:
13                    res.append(str(start))
14                else:
15                    res.append(str(start) + "->" + str(end))
16                start = n
17                end = n
18        if start == end:
19            res.append(str(start))
20        else:
21            res.append(str(start) + "->" + str(end))
22        return res