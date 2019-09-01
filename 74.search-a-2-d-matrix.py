#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        n = len(matrix)
        m = len(matrix[0])
        low,high = 0,n*m-1
        while(low <= high):
            
            mid = (low+high)//2
            i,j = divmod(mid,m)
            if target==matrix[i][j]:
                return True
            if target> matrix[i][j]:
                low = mid+1
            else: high = mid-1
        return False

            
