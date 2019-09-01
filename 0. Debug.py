#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix: return False
        n = len(matrix)
        m = len(matrix[0])
        low,high = 0,n*m-1
        while(low < high):
            mid = (low+high)//2
            i,j = divmod(mid,m)
            if target==matrix[i][j]:
                return True
            if target> matrix[i][j]:
                low = mid+1
            else: high = mid-1
        return False


                
s = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(s.searchMatrix(matrix,target))