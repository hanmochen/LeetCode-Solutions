#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        curSum = 0
        maxSum = float('-inf')
        for num in nums:
            curSum = (curSum+num) if(curSum>0) else num
            maxSum = max(maxSum,curSum)

        return maxSum

