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
                
                next[r] = next[k] if(pattern[r]== pattern[k]) else k
            return next

        if not needle: return 0
        next = findNext(needle)
        i,j = 0,0
        while(i<len(haystack) and j<len(needle)):
            if(j== -1 or haystack[i] == needle[j]):
                i += 1
                j += 1
            else:
                j = next[j]
        return i-j if(j == len(needle)) else -1 

