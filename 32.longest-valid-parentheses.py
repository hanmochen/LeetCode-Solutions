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
        dp = l*[-1]
        maxLength = 2
        for index in range(1,l):
            if s[index]== ')':
                left = index-1
                if(s[left] == '('):
                    if(left == 0 or s[left-1] == '('):
                        dp[index]=left
                    else:
                        dp[index]=dp[left-1] if(dp[left-1]!= -1) else left
                        maxLength = max(maxLength,index-dp[index]+1)
                else:
                    if dp[left]<= 0:
                        dp[index] = -1
                    elif s[dp[left]-1]=='(':
                        left = dp[left]-1
                        dp[index]=dp[left-1] if(dp[left-1]!= -1) else left
                        maxLength = max(maxLength,index-dp[index]+1)

        return maxLength
            

