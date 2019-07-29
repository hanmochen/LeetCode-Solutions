#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        count = 0
        while(count < len(nums)):
            if nums[count] == val: nums.pop(count)
            else : count += 1
        return count

