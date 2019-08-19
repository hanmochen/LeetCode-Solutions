#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mergedIntervals = sorted(intervals,key= lambda x: x[0])
        index = 0
        while(index< len(mergedIntervals)-1):
            if mergedIntervals[index][1]>= mergedIntervals[index+1][0]:
                mergedInterval = [mergedIntervals[index][0],max(mergedIntervals[index][1],mergedIntervals[index+1][1])]
                mergedIntervals[index+1]= mergedInterval
                mergedIntervals.pop(index)

            else: index += 1
        return mergedIntervals

        

