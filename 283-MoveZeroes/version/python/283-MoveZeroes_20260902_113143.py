# Last updated: 02/09/2026, 11:31:43
1class Solution:
2    def longestConsecutive(self, nums):
3        if not nums:
4            return 0
5
6        nums.sort()
7        ans = 1
8        consecutive_size = 1
9        for i in range(1, len(nums)):
10            if nums[i-1] == nums[i]: continue
11            if nums[i-1] + 1 == nums[i]:
12                consecutive_size += 1
13            else:
14                ans = max(ans, consecutive_size)
15                consecutive_size = 1
16
17        ans = max(ans, consecutive_size)
18        return ans