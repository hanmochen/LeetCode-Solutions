#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        for index in range(len(nums)):
            while 0<nums[index]<=len(nums) and nums[index]!= nums[nums[index]-1]:
                temp = nums[nums[index]-1]
                nums[nums[index]-1]= nums[index]
                nums[index] = temp
    
        for index,num in enumerate(nums):
            if index+1 != num:
                return index+1
        
        return len(nums)+1
        
        
            


