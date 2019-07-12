#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

from math import log10 as log
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0): return False
        if(x==0): return True
        numOfDigits = int(log(x))
        rangeTen = 10**numOfDigits
        while(x>0):            
            if(x%10 !=  int(x/rangeTen)): return False
            x = int((x%rangeTen) /10)
            rangeTen /= 100
        
        return True
        

#sol = Solution()
#sol.isPalindrome(121)
