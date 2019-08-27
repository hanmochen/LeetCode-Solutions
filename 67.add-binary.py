#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(a,b,c):
            if a or b or c:
                ans = (len(a) and a[-1] == '1') + ( len(b) and b[-1]=='1') + c
                return add(a[:-1],b[:-1],ans//2)+str(ans%2)
            return ''
        return add(a,b,0)        

            

        

        

