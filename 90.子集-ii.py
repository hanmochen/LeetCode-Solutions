#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        res = [[]]
        while(nums):
            num = nums.pop(0)
            sets = [[],[num]]
            lastSet = [num]
            while(nums and nums[0] == num):              
                lastSet.append(nums.pop(0))
                sets.append(lastSet.copy())
            res = [x+y for x in res for y in sets]
        return res   


# @lc code=end

