#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1): return s
        period = 2*(numRows - 1)
        length = len(s)-1
        result = ""
        rounds = int (length/period)
        remains = length % period 

        for i in range(rounds+1):
            result += s[i*period]

        if(remains<numRows-1):
            for j in range(1,remains+1):
                for i in range(rounds):
                    result += s[j+i*period]
                    result += s[(i+1)*period-j]

                result += s[j+rounds*period]
            
            for j in range(remains+1,numRows-1):
                for i in range(rounds):
                    result += s[j+i*period]
                    result += s[(i+1)*period-j]
                    
            for i in range(rounds):
                result += s[numRows-1+i*period]

        else:
            for j in range(1,period-remains):
                for i in range(rounds):
                    result += s[j+i*period]
                    result += s[(i+1)*period-j]

                result += s[j+rounds*period]
            
            for j in range(period-remains,numRows-1):
                for i in range(rounds):
                    result += s[j+i*period]
                    result += s[(i+1)*period-j]  

                result += s[j+rounds*period]
                result += s[rounds*period+period-j]

            for i in range(rounds):
                result += s[numRows-1+i*period]
                
            result += s[numRows-1+rounds*period]
        return result
