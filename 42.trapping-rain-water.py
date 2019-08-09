#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        maxLeft = maxRight = 0
        volume = 0
        while(left<=right):
            maxLeft = max(maxLeft,height[left])
            maxRight = max(maxRight,height[right])
            if maxLeft<maxRight:
                volume += min(maxLeft,maxRight) - height[left]
                left += 1
            else:
                volume += min(maxLeft,maxRight)-height[right]
                right -= 1
        return volume