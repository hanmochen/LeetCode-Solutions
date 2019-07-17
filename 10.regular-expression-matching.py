#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        
        lengthOfText,lengthOfPattern = len(text),len(pattern)
        dp = [[False]* (lengthOfPattern + 1) for _ in range(lengthOfText+1)] 
        dp[-1][-1] = True #End of Match

        for i in range(lengthOfText,-1,-1):
            for j in range(lengthOfPattern-1,-1,-1):
                if(j == lengthOfPattern-1):
                    dp[i][j] = ( (i == lengthOfText-1) and (self.isMatchOfSingleCharacter(text[i],pattern[j])) )
                else:
                    if(pattern[j+1] == '*'):
                        if(i == lengthOfText ): # End of Text
                            dp[i][j] = dp[i][j+2]
                        else:
                            dp[i][j] = (dp[i][j+2] or (self.isMatchOfSingleCharacter(text[i],pattern[j]) and dp[i+1][j]))
                    else:
                        if(i == lengthOfText): dp[i][j] = False
                        else:
                            dp[i][j] = dp[i+1][j+1] and (self.isMatchOfSingleCharacter(text[i],pattern[j]) )
                        
        return dp[0][0]
        
    def isMatchOfSingleCharacter(self,textCharacter,patternCharacter)->bool:
                return patternCharacter == '.' or patternCharacter == textCharacter