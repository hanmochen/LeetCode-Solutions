#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        temp = nums[0]
        pos = 1
        index = 1

        while(index < len(nums)):
            nums[pos] = nums[index]
            pos += 1
            if nums[index] == temp:  
                index += 1  
                while index<len(nums) and  nums[index] == temp:
                    index += 1
            else:
                temp = nums[index]
                index += 1
        
        return pos



