#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        
        xn = x
        while(xn*xn>x):
            xn = (xn+x/xn)//2
        return(int(xn))




