#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if not nums: return 0
        temp = nums[0]
        pos = 1
        index = 1

        while(index < len(nums)):
            count = nums[index] == temp 
            nums[pos] = nums[index]
            pos += 1
            temp = nums[index]
            index += 1
            if count:                
                while index<len(nums) and  nums[index] == temp:
                    index += 1
        
        return pos


                
s= Solution()
nums = [0]

print(s.removeDuplicates(nums))
print(nums)
