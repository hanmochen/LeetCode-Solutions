#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        height = len(grid)
        width = len(grid[0])
        paths = [(width+1)*[float('inf')] for _ in range(height+1)]
        paths[-2][-1]=0
        for n in range(height-1,-1,-1):
            for m in range(width-1,-1,-1):
                paths[n][m] = grid[n][m] + min(paths[n+1][m],paths[n][m+1])
        
        return paths[0][0]


