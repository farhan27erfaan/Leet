# Last updated: 11/08/2026, 11:43:17
class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        max_water=0
        while left<right:
            water=min(height[left],height[right])*(right-left)
            max_water=max(max_water,water)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water
      