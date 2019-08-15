#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0 : 
            n = -n
            x = 1/x
        multiplier = x
        answer = 1.0
        while n > 0 :
            answer = answer*multiplier if(n%2) else answer
            n = n>>1
            multiplier = multiplier*multiplier
        return answer


