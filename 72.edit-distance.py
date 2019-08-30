#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if not word1: return len(word2)
        # if not word2: return len(word1)
        # if word1[-1] == word2[-1]:
        #     return self.minDistance(word1[:-1],word2[:-1])
        # return 1+min(self.minDistance(word1[:-1],word2[:-1]),self.minDistance(word1[:-1],word2),self.minDistance(word1,word2[:-1]))
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word1)+1):
            dp[0][i] = i
        for i in range(len(word2)+1):
            dp[i][0] = i
        
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                dp[i][j] = dp[i-1][j-1] if word1[j-1] == word2[i-1] else 1+min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
        return dp[-1][-1]
             
        

