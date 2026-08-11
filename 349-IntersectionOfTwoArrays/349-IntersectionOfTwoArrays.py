# Last updated: 11/08/2026, 11:40:50
class Solution(object):
    def intersection(self, nums1, nums2):
      n1=len(nums1)
      n2=len(nums2)
      new=set()
      for i in range(n1):
        for j in range(n2):
            if nums1[i]==nums2[j]:
                new.add(nums2[j])
      return list(new)

