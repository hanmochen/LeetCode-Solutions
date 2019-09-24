#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
class Solution:
    def search(self, nums: [int], target: int) -> bool:
        if not nums: return False

        low, high = 0, len(nums)

        while(low < high):
            mid = ( low + high ) // 2
            if(nums[mid] == target): return True
            
            if( (nums[mid]<nums[0]) == (target < nums[0]) ):
                if(nums[mid]>target): high = mid
                else: low = mid+1
            
            elif(nums[mid]>target): low = mid+1
            else: high = mid
        
        return False
                
s= Solution()
nums = [1,3,1,1]
target = 3
print(s.search(nums,target))

