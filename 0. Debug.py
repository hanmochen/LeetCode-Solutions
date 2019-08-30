#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        result = []
        for dire in dirs:
            if dire and dire != '.' : 
                if dire == '..' : result = result[:-1]
                else: result.append(dire)
        return '/'+'/'.join(result)
                
s = Solution()
print(s.simplifyPath("/home/"))