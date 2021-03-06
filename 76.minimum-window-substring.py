#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t: return ''
        dicT = {}
        for char in t:
            if char in dicT:
                dicT[char] += 1
            else: dicT[char] = 1
        left = 0
        while(left<len(s) and s[left] not in dicT):
            left += 1
        if left == len(s): return ''
        right = left
        subDic = {}
        setT = set(dicT.keys())
        pos = []
        while(setT):
            if right == len(s): return ''
            if s[right] in dicT:
                pos.append(right)
                if s[right] in subDic:
                    subDic[s[right]] += 1
                else: subDic[s[right]] = 1
                if subDic[s[right]] == dicT[s[right]]:
                    setT.remove(s[right])   
            right += 1

        window = s[left:right]
        pos.pop(0)

        while(right <= len(s)):
            
            while(subDic[s[left]] > dicT[s[left]]):
                subDic[s[left]] -= 1
                left = pos.pop(0)
                if right-left < len(window):
                    window = s[left:right]

            subDic[s[left]] -= 1
            while(subDic[s[left]] < dicT[s[left]]):
                if right == len(s): return window
                if s[right] in dicT:
                    pos.append(right)
                    subDic[s[right]] += 1
                right += 1
            left = pos.pop(0)
            if right-left < len(window):
                window = s[left:right]
    

        return window




        



