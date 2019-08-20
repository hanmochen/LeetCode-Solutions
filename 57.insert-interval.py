#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        from bisect import bisect_left, bisect_right
        beginIndex = bisect_left([interval[1] for interval in intervals],newInterval[0])
        endIndex = bisect_right([interval[0] for interval in intervals],newInterval[1])
        if beginIndex < endIndex:
            newInterval = [min(intervals[beginIndex][0],newInterval[0]),max(intervals[endIndex-1][1],newInterval[1])]
            intervals = intervals[:beginIndex]+[newInterval]+intervals[endIndex:]
        else:
            intervals.insert(beginIndex,newInterval)
        return intervals


