# Last updated: 11/08/2026, 11:40:14
class Solution(object):
    def angleClock(self, hour, minutes):
        hour=hour%12
        hour_angle=hour*30+minutes*0.5
        minute_angle=minutes*6
        diff=abs(hour_angle-minute_angle)
        return min(diff,360-diff)
        