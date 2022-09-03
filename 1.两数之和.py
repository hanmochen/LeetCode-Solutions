#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, num in enumerate(nums):
            if (target-num) in dct:
                return [dct[target-num], i]
            dct[num] = i
        return []
# @lc code=end

