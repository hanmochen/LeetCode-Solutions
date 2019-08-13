#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<2: return [nums]
        def nextPermutation():
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

            nums[0] = None
            return

        nums.sort()
        res = []
        while nums[0] is not None:
            res.append(nums[:])
            nextPermutation()
            
        return res
        
