#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        def count(string):
            countStr = ''
            lastChar = string[0]
            count = 0 
            for char in string:
                if char == lastChar:
                    count += 1
                else:
                    countStr +=  str(count) + lastChar
                    lastChar = char 
                    count = 1
            countStr += str(count) + lastChar
            return countStr
        
        countStr = '1'
        if n == 1: return countStr
    
        while(n>1):
            countStr = count(countStr)
            n -= 1
        
        return countStr
                    