#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def combinationNumber(n,m):
            m = m if m<n-m else n-m
            if m == 0: return 1
            up,down,ans = n,1,1
            while(m>0):
                ans = (ans*up)//down
                up -= 1
                down += 1
                m -= 1
            return ans
        
        return combinationNumber(m+n-2,m-1)

