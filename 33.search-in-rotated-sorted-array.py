#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if nums[0] == target: return 0
        
        low, high = 0, len(nums)

        while(low < high):
            mid = ( low + high ) // 2
            if(nums[mid] == target): return mid
            
            if( (nums[mid]<nums[0]) == (target < nums[0]) ):
                if(nums[mid]>target): high = mid
                else: low = mid+1
            
            elif(nums[mid]>target): low = mid+1
            else: high = mid
        
        return -1 



