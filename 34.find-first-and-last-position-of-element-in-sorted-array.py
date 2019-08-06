#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        def findLeftBound():    
            low,high=0,len(nums)-1
            if nums[low]>= target: return -1
            if nums[high]< target: return high
            while(low<high-1):
                mid = (low + high) // 2
                if(nums[mid]<target):
                    low = mid
                else: high = mid
            return low
        
        left = findLeftBound()
        def findRightBound():
            low,high=left,len(nums)-1
            if nums[high]<= target: return high+1
            while(low<high-1):
                mid = (low + high) // 2
                if(nums[mid]<=target):
                    low = mid
                else: high = mid
            return high
        
        right = findRightBound()
        if left >= right - 1: return [-1,-1]
        else: return [left+1,right-1]
           

