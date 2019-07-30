#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def findNext(pattern: str)-> [int]:
            next = len(pattern)*[-1]
            r,k = 0,-1
            while(r<len(pattern)-1):
                while(k>=0 and pattern[r] != pattern[k]):
                    k = next[k]
                k += 1
                r += 1
                next[r] = k
            return next

        def KMP(text:str, pattern: str )-> int:
            next = findNext(pattern)
            i,j = 0,0
            while(i<len(text) and j<len(pattern)):
                if(j== -1 or text[i] == pattern[j]):
                    i += 1
                    j += 1
                else:
                    j = next[j]
            if(j == len(pattern)):return i-j
            else: return -1

        return KMP(haystack,needle)

