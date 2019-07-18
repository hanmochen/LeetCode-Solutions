#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        romanNumber = ""
        while(num>=1000):
            num -= 1000
            romanNumber += "M"
        romanNumber += self.oneDigitIntToRoman(num//100,"C","D","M")
        num = num%100
        romanNumber += self.oneDigitIntToRoman(num//10,"X","L","C")
        num = num%10 
        romanNumber += self.oneDigitIntToRoman(num,"I","V","X")
        return romanNumber
        

    def oneDigitIntToRoman(self,num:int,oneRoman:str,fiveRoman:str,tenRoman:str)->str:

        if(num in {4,9}):
            oneDigitRoman = oneRoman
            if(num>4):
                oneDigitRoman += tenRoman
            else: oneDigitRoman += fiveRoman
        else:
            oneDigitRoman = (num//5)*fiveRoman + (num%5) * oneRoman
        return oneDigitRoman



