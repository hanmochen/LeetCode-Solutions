#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2: return

        def swap4(i,j):
            matrix[i][j], matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i] = matrix[n-1-j][i],matrix[i][j], matrix[j][n-1-i],matrix[n-1-i][n-1-j]

        for row in range(0,n//2):
            for col in range(row,n-row-1):
                swap4(row,col)
        
        return


