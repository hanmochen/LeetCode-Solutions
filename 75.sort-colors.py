#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
class Solution:
    def sortColors(self, nums:[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros,ones=-1,-1
        for index,num in enumerate(nums):
            nums[index] = 2
            if num == 0:
                zeros += 1
                ones += 1
                nums[ones] = 1
                nums[zeros] = 0
            elif num == 1:
                ones += 1
                nums[ones] = 1
        
        return

