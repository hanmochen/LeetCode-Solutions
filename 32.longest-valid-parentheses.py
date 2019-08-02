#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        indexStack = [-1]
        maxLen = 0
        for index,char in enumerate(s):
            if char == '(':
                indexStack.append(index)
            else:
                indexStack.pop()
                if indexStack:
                    lastIndex = indexStack[-1]
                    maxLen = max(maxLen,index-lastIndex)
                else:
                    indexStack.append(index)          
        return maxLen
