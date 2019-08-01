#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        for index in range(len(nums)-1,0,-1):
            if nums[index] > nums[index-1]:
                ind = index
                while(ind<len(nums) and nums[ind]>nums[index-1]):
                    ind += 1
                nums[ind-1],nums[index-1] = nums[index-1],nums[ind-1]# Swap
                temp = nums[index:]
                temp.reverse()
                nums[index:] = temp
                return

        nums.reverse()
        return


