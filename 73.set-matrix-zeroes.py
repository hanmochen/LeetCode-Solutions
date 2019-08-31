#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        if not matrix: return 

        rowflag = 0
        colflag = 0
        for col in range(len(matrix)):
            if matrix[col][0] == 0:
                colflag = 1
        for row in range(len(matrix[0])):
            if matrix[0][row] == 0:
                rowflag = 1
        for col in range(1,len(matrix)):
            for row in range(1,len(matrix[0])):
                if not matrix[col][row]:
                    matrix[col][0] = 0
                    matrix[0][row] = 0  


        for col in range(1,len(matrix)):
            for row in range(1,len(matrix[0])):
                if matrix[col][0]==0 or matrix[0][row]==0 :
                   matrix[col][row] = 0
        
        
        for col in range(len(matrix)):
            if colflag:
                matrix[col][0] = 0
        if rowflag:
            matrix[0] = len(matrix[0])*[0]
        
        return

        

