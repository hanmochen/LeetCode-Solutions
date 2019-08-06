#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        low, high = 0, len(nums)-1
        if(nums[low]>= target): return 0
        if(nums[high]< target): return high+1
        while(low<high-1):
            mid = (low+high) // 2
            if(nums[mid]> target):
                high = mid
            elif(nums[mid]<target):
                low = mid
            else: return mid
        if(target== nums[low]): return low
        return high


