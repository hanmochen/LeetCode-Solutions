#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t: return ''
        def createDic(T):
            dic = {}
            for char in T:
                if char in dic:
                    dic[char] += 1
                else: dic[char] = 1
        
        dicT = createDic(t)

        left = 0
        while(left<len(s) and s[left] not in dicT):
            left += 1
        if left == len(s): return ''
        
        right = left
        dic = dicT.copy()
        pos = []
        while(dic is not None):
            if right == len(s): return ''
            if s[right] in dicT:
                pos.append(right)
                if s[right] in dic:
                    if dic[s[right]] == 1:
                        del dic[s[right]]
                    else: dic[s[right]] -= 1
            right += 1

        window = s[left:right]

        while(right <= len(s)):
            if right == len(s): return window
            if s[right]






        



