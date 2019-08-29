#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        return round(0.2**0.5*((1.25**0.5+0.5)**(n+1)))

