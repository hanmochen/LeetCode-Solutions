#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        expressionStack = []
        bracketDictionary = {"}":"{",
                             "]":"[",
                             ")":"("}
        if not s: return True
        for char in s:
            if char in bracketDictionary:
                if not expressionStack: return False
                if( bracketDictionary[char]!= expressionStack.pop()): return False
            else: expressionStack.append(char)
        
        return not expressionStack
                

