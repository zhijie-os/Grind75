# 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 0
        interval = points[0]
        for i in range(1, len(points)):
            if points[i][0] <= interval[1] and points[i][0] >= interval[0]:
                interval[0] = max(interval[0], points[i][0])
                interval[1] = min(interval[1], points[i][1])
            else:
                interval = points[i]
                count += 1
        return count + 1