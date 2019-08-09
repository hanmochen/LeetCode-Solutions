#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3: return 0
        maxValue = max(height[1:-1])
        if maxValue<height[0] and maxValue<height[-1]:
            h = min(height[0],height[-1])
            return (len(height)-2)*h - sum(height[1:-1])
        else:
            maxIndex = height[1:-1].index(maxValue)+1
            return self.trap(height[:maxIndex+1])+self.trap(height[maxIndex:])

