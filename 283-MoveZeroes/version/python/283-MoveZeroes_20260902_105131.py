# Last updated: 02/09/2026, 10:51:31
1class Solution(object):
2    def canPlaceFlowers(self, flowerbed, n):
3        flowerbed_size = len(flowerbed)
4        for i in range(flowerbed_size):
5            if n <= 0:
6                break
7            prev = i == 0 or flowerbed[i - 1] == 0
8            fut = i == flowerbed_size - 1 or flowerbed[i + 1] == 0
9            if prev and fut and flowerbed[i] == 0:
10                flowerbed[i] = 1
11                n -= 1
12        return n <= 0