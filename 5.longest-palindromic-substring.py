#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #preprocessing
        s1='#'+'#'.join(s)+'#'
        radius=[1]*len(s1)
        rightBound,centerPosition,maxLength,maxPosition=1,0,1,0

        for i in range(len(s1)):
            if(i+maxLength>len(s1)):break
            iMirrored = 2*centerPosition - i
            if(radius[iMirrored]>=rightBound-i):
                radius[i] = rightBound-i
                while(i-radius[i]>=0 and i+radius[i]< len(s1) and s1[i+radius[i]] == s1[i-radius[i]]):
                    radius[i] += 1
                centerPosition = i
                rightBound = i + radius[i]
            else: radius[i]=radius[iMirrored]
            
            if(radius[i]>maxLength):
                maxLength = radius[i]
                maxPosition = i
        
        maxLength -= 1
        return s[int((maxPosition-maxLength)/2):int((maxPosition+maxLength)/2)]


