# Last updated: 11/08/2026, 11:42:16
class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(n-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
       
        

 
        