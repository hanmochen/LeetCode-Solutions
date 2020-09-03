#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '': return 0
        dp = [1 for i in range(len(s))]
        dp[0] = 1 if '1'<= s[0] <= '9' else 0
        for i in range(1,len(s)):
            if '1' <= s[i] <= '9':
                dp[i] = dp[i-1]+dp[i-2]  if 11 <= int(s[i-1:i+1]) <= 26 else dp[i-1]
            elif s[i] == '0' and '1'<= s[i-1] <= '2':
                dp[i] = dp[i-2]
            else: dp[i] = 0          
        return dp[-1]


# @lc code=end

