#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1): return s
        n = 2*(numRows - 1)
        l = len(s)-1
        res = ""
        rounds = int (l/n)
        remained = l % n 

        for i in range(rounds+1):
            res += s[i*n]

        if(remained<numRows-1):
            for j in range(1,remained+1):
                for i in range(rounds):
                    res += s[j+i*n]
                    res += s[(i+1)*n-j]

                res += s[j+rounds*n]
            
            for j in range(remained+1,numRows-1):
                for i in range(rounds):
                    res += s[j+i*n]
                    res += s[(i+1)*n-j]
                    
            for i in range(rounds):
                res += s[numRows-1+i*n]

        else:
            for j in range(1,n-remained):
                for i in range(rounds):
                    res += s[j+i*n]
                    res += s[(i+1)*n-j]

                res += s[j+rounds*n]
            
            for j in range(n-remained,numRows-1):
                for i in range(rounds):
                    res += s[j+i*n]
                    res += s[(i+1)*n-j]  

                res += s[j+rounds*n]
                res += s[rounds*n+n-j]

            for i in range(rounds):
                res += s[numRows-1+i*n]
                
            res += s[numRows-1+rounds*n]
        return res
