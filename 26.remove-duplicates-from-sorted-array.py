#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        prev = nums[0]
        count = 1
        while(count < len(nums)):
            if nums[count] != prev:
                prev = nums[count]
                count += 1
            else: 
                nums.pop(count)
        return count
            
