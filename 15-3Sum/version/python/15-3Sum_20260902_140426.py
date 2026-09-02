# Last updated: 02/09/2026, 14:04:26
1class Solution:
2    def threeSum(self, nums):
3        re = []
4        nums.sort()
5        n = len(nums)
6
7        for i in range(n):
8            if nums[i] > 0:
9                break
10
11            if i > 0 and nums[i] == nums[i-1]:
12                continue
13
14            l, r = i+1, n-1
15
16            while l < r:
17                su = nums[i] + nums[l] + nums[r]
18
19                if su > 0:
20                    r -= 1
21                elif su < 0:
22                    l += 1
23                else:
24                    re.append([nums[i], nums[l], nums[r]])
25                    l += 1
26                    r -= 1
27
28                    while l < r and nums[l] == nums[l-1]:
29                        l += 1
30                    while l < r and nums[r] == nums[r+1]:
31                        r -= 1
32
33        return re