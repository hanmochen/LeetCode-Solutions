

#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        if not nums: return [[]]

        a = nums.pop()
        res = []
        for subset in self.subsets(nums):
            res.append(subset.copy())
            subset.append(a)
            res.append(subset)
        return res

s= Solution()
nums = [1,2,3]
print(s.subsets(nums))
