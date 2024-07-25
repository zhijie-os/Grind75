class Solution:
   def merge(self, intervals):
        intervals.sort()
        interval = intervals[0]
        result = []
        for i in range(len(intervals)):
            if intervals[i][0] <= interval[1]:
                interval[1] = max(intervals[i][1], interval[1])
            else:
                result.append(interval)
                interval = intervals[i]
            
        result.append(interval)
        return result