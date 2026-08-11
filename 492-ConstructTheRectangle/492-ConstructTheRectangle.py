# Last updated: 11/08/2026, 11:40:43
class Solution:
    def constructRectangle(self, area):
        w = int(area ** 0.5)

        while area % w != 0:
            w -= 1

        return [area // w, w]