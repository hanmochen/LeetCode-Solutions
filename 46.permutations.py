#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=1: return [nums]
        allPermutations = []
        for permutation in self.permute(nums[1:]):
            for index in range(len(nums)):
                s= permutation.copy()
                s.insert(index,nums[0])
                allPermutations.append(s)
        return allPermutations



