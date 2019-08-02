#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
            if len(nums)<=3:
                try:
                    return nums.index(target)
                except ValueError:
                    return -1
            
            def findMaxIndex(nums)-> int:
                left,right = 0, len(nums)-1
                while(left<right):
                    mid = (left+right) // 2
                    if nums[mid]>nums[mid+1]: return mid
                    elif nums[mid]>nums[right]: left = mid
                    else: right = mid
                return -1 
                        
            def binary_search(nums,left,right,target)->int:
                if(nums[left]>target or nums[right]<target): return -1
                while(left<right):
                    mid = (left+right) // 2
                    if nums[mid]==target: return mid
                    elif right-left == 1 : break
                    elif nums[mid]<target: left = mid
                    else: right = mid
                return right if(nums[right]==target) else -1

            maxIndex = findMaxIndex(nums)
            if(maxIndex == -1):
                return binary_search(nums,0,len(nums)-1,target)
            
            if(target<nums[0]):
                return binary_search(nums,maxIndex+1,len(nums)-1,target)
            else: 
                return binary_search(nums,0,maxIndex,target)


        




