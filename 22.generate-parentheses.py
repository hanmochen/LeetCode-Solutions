#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 2 : return [n*"()"]
        validSet = []
        for i in range(n):            
            validSet += ["("+str1+")"+str2 for str1 in self.generateParenthesis(i) for str2 in self.generateParenthesis(n-1-i)]
        return validSet


