# Last updated: 11/08/2026, 11:42:10
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
        