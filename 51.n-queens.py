#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(positions,sums,diffs):
            m = len(positions)
            if m == n:
                solutions.append(positions)
                return
            for i in range(n):
                if not (i in positions or (m+i) in sums or (m-i) in diffs):
                    DFS(positions+[i],sums+[m+i],diffs+[m-i])
        solutions=[]
        DFS([],[],[])

        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in solutions]




  

