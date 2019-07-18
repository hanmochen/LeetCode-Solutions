#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntDictionary = {'I':1, 'V':5, 'X':10, 'L':50 , 'C':100, 'D':500, 'M':1000}
        intNumber = romanToIntDictionary[s[-1]]
        for index in range(len(s)-1):
            if(romanToIntDictionary[s[index]]<romanToIntDictionary[s[index+1]]):
                intNumber -= romanToIntDictionary[s[index]]
            else: intNumber += romanToIntDictionary[s[index]]
        return intNumber
  

