
# @lc app=leetcode id=29 lang=python3

# [29] Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1 : return dividend
        INT_MAX = 2**31 -1
        INT_MIN = - 2**31
        if divisor == -1 : 
            return -dividend if dividend != INT_MIN else INT_MAX
        flag = (divisor>0 and dividend >0) or (divisor<0 and dividend <0) 
        absOfDividend = abs(dividend)
        absOfDivisor = abs(divisor)
        if(absOfDividend<absOfDivisor): return 0

        def findMaxPower(divisor:int,dividend:int)-> int:
            low = 0
            high = 31
            res = 15
            while(divisor<<(res+1) <= dividend or divisor<<res > dividend):
                if divisor<<(res+1) == dividend: return res+1
                elif divisor<<(res+1) < dividend:
                    low = res+1  
                elif divisor<<res > dividend:
                    high = res
                res = (high+low)>>1
            return res
        
        nPowers = findMaxPower(absOfDivisor,absOfDividend)
        powersOfTwo = 1<<nPowers
        multipliers = absOfDivisor<<nPowers    
        times = 0
        remains = absOfDividend
        while(remains>=absOfDivisor):
            if remains>= multipliers :
                remains -= multipliers
                times += powersOfTwo
            multipliers >>= 1
            powersOfTwo >>= 1
        
        return times if flag else -times

