#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = s.lstrip(')').rstrip('(')
        if not s: return 0
        l = len(s)
        dp = l*[0]
        for index in range(1,l):
            if s[index]== ')':
                if(s[index-1] == '('):
                    dp[index]=2 if(index == 1) else dp[index-2]+2 
                else:
                    left = index-1-dp[index-1]
                    dp[index] = 0 if(left < 0 or s[left] == ')') else dp[left-1]+dp[index-1]+2
        return max(dp)

