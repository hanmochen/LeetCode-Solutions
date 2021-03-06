#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
class Solution:
    def myAtoi(self, str: str) -> int:
        l = len(str)
        INT_MAX = 2**31-1
        INT_MIN = - 2**31
        if(l == 0): return 0
        
        pos = 0 
        flag = True
        res = 0
        while(pos < l and str[pos]==" "): 
            pos += 1
        
        if(pos>=l): return 0

        if(not( str[pos]=="+" or str[pos] == "-" or (str[pos]>= "0" and str[pos] <= "9"))): return 0
        
        if( str[pos]=="+" or str[pos] == "-"): 
            flag = (str[pos]== "+")
            pos += 1
        

        while (pos < l and str[pos]>="0" and str[pos] <= "9" ):
            if(res>INT_MAX or res < INT_MIN):
                if flag: return INT_MAX
                else: return INT_MIN
            
            res *= 10
            res += int(str[pos]) - int("0")
            pos += 1

        if(res>INT_MAX or res < INT_MIN):
                if flag: return INT_MAX
                else: return INT_MIN
        
        if flag: return res
        else: return -res
        
# sol = Solution()
# s = " "
# print(sol.myAtoi(s))
