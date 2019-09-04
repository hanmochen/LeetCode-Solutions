#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]

        a = nums.pop()
        res = []
        for subset in self.subsets(nums):
            res.append(subset.copy())
            subset.append(a)
            res.append(subset)
        return res

            

        

