#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = s.lstrip(')').rstrip('(')
        maxLen = 0 
        left = right = 0
        for index,char in enumerate(s):
            if(char == '('):
                left += 1
            else:
                right += 1
            if left == right :
                maxLen = max(maxLen,right)
            elif right > left:
                left = right = 0
        left = right = 0
        for index,char in enumerate(s[::-1]):  
            if(char == '('):
                left += 1
            else:
                right += 1
            if left == right :
                maxLen = max(maxLen,right)
            elif left > right:
                left = right = 0
        return 2*maxLen
