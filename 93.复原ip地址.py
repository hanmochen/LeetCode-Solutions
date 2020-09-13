#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(s:str)-> bool:
            if len(s) == 1: return True
            if len(s) == 2 and s[0] != '0': return True
            if len(s) == 3 and 99 < int(s) < 256: return True
            return False
        def getIP(s:str,n:int) -> [str]:
            if n == 1: 
                return [s] if isValid(s) else []
            possibleIP = []
            for i in range(1,4):
                if (n-1) <= len(s)-i <= 3*(n-1) and isValid(s[0:i]):
                    possibleIP += [s[0:i] + '.' + ip for ip in getIP(s[i:],n-1)]
            return possibleIP
        return getIP(s,4)       
            
# @lc code=end

