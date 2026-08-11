# Last updated: 11/08/2026, 11:43:22
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        merged_array = nums1 + nums2
        merged_array.sort()

        n = len(merged_array)

        if n % 2 == 1:
            return float(merged_array[n // 2])

        else:
            mid1 = merged_array[n // 2 - 1]
            mid2 = merged_array[n // 2]

            return (mid1 + mid2) / 2.0
        