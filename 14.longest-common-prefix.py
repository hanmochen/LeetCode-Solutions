#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(not strs):return ""
        commonPrefix = ""
        #shortestLength = min([len(strs[i]) for i in range(len(strs))])
        shortestString = min(strs,key=len)
        for indexOfChar,currentChar in enumerate(shortestString):
            for str in strs:
                if (str[indexOfChar]!= currentChar):
                    return commonPrefix
            commonPrefix += currentChar
        return commonPrefix
        

