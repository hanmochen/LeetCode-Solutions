#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def findLargestArea(begin: int, end: int):
            if begin == end: return 0
            if begin == end+1: return heights[begin]
            mid = (begin + end)//2
            left = mid
            right = mid+1
            minHeight = heights[mid]
            area = heights[mid]
            while(left > begin or right <end):
                if(left > begin and right < end):
                    if heights[left-1] >= heights[right]:
                        minHeight = min(minHeight,heights[left-1])
                        left -= 1
                    else: 
                        minHeight = min(minHeight,heights[right])
                        right += 1
                    area = max(area,minHeight*(right - left))
                
                elif left == begin:
                    while(right < end):
                        minHeight = min(minHeight,heights[right])
                        right += 1
                        area = max(area,minHeight*(right - left))
                
                else:
                    while(left>begin):
                        minHeight = min(minHeight,heights[left-1])
                        left -= 1
                        area = max(area,minHeight*(right - left))

            return max(findLargestArea(begin,mid),findLargestArea(mid+1,end),area)   
        return findLargestArea(0,len(heights))



        
# @lc code=end

