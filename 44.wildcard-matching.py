#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = (len(s)+1)*[False]
        flag = (len(s)+1)*[False]

        dp[-1]= True

        for i in range(len(p)-1,-1,-1):
            flag[-1]= dp[-1]
            for j in range(len(s)-1,-1,-1):
                flag[j] = flag[j+1] or dp[j]
            for j in range(len(s)+1):
                if p[i] == '*':
                    dp[j] = flag[j]
                else:
                    dp[j] = (j!= len(s)) and (p[i]== '?' or p[i] == s[j]) and dp[j+1]
        
        return dp[0]


