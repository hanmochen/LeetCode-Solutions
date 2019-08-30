#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for dire in path.split('/'):
            if dire and dire != '.' : 
                if dire == '..' : 
                    if result: result.pop()
                else: result.append(dire)
        return '/'+'/'.join(result)
                
        

