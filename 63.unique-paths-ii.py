#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        paths = [(width+1)*[0] for _ in range(height+1)]
        paths[-2][-1] = 1
        for n in range(height-1,-1,-1):
            for m in range(width-1,-1,-1):
                paths[n][m] = 0 if obstacleGrid[n][m] else paths[n+1][m]+paths[n][m+1]
        
        return paths[0][0]



        
        

