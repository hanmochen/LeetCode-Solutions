#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        flag = (x>=0)
        INT32_MAX = 2**31-1
        INT32_MIN = - 2**31
        x = abs(x)
        res = 0
        if x==0 : return res
        while(x!=0):
            res *= 10
            tmp = x %10
            res += tmp
            x = int(x/10)

        if not flag: res = -res
        if res >= INT32_MAX or res <= INT32_MIN: res = 0
        
        return res


