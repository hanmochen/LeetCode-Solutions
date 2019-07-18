#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        rightBoundIndex = len(height)-1
        leftBoundIndex = 0
        maxArea = min(height[leftBoundIndex],height[rightBoundIndex])*(rightBoundIndex-leftBoundIndex)

        while leftBoundIndex < rightBoundIndex:
            if height[leftBoundIndex] < height[rightBoundIndex]:# If left is higher than right, then move the left bound
                leftBoundIndex += 1         
            else: rightBoundIndex -= 1
            
            maxArea = max(maxArea,min(height[leftBoundIndex],height[rightBoundIndex])*(rightBoundIndex-leftBoundIndex))

        return maxArea
            

