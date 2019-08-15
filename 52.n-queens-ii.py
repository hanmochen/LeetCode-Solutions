#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        count = 0
        def DFS(positions,sums,diffs):
            m = len(positions)
            nonlocal count
            if m == n:
                count += 1
                return
            for i in range(n):
                if not (i in positions or (m+i) in sums or (m-i) in diffs):
                    DFS(positions+[i],sums+[m+i],diffs+[m-i])

        DFS([],[],[])

        return count




  

       

