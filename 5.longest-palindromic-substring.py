#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #预处理
        s1='#'+'#'.join(s)+'#'
        RL=[0]*len(s1)
        MaxRight=0
        pos=0
        MaxLen=0
        maxPos=0
        for i in range(len(s1)):
            if i<MaxRight:
                RL[i]=min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i]=1
            #尝试扩展，注意处理边界
            while i-RL[i]>=0 and i+RL[i]<len(s1) and s1[i-RL[i]]==s1[i+RL[i]]:
                RL[i]+=1
            #更新MaxRight,pos
            if RL[i]+i-1>MaxRight:
                MaxRight=RL[i]+i-1
                pos=i
            #更新最长回文串的长度
            if RL[i]>MaxLen:
                MaxLen = RL[i]
                maxPos = i

        MaxLen = MaxLen - 1
        return s[int((maxPos-MaxLen)/2):int((maxPos+MaxLen)/2)]
        # if maxPos%2 == 0:
        #     pos = int(maxPos/2)
        #     half = int(MaxLen/2)
        #     return s[pos-half:pos+half]
        # else:
        #     pos = int(maxPos/2)
        #     half = int(MaxLen/2)
        #     return s[pos-half:pos+half+1]

