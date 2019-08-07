#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(listOfNums):
            res = [i for i in listOfNums if i != '.']
            return len(res) == len(set(res))
        
        for row in board:
            if not isValid(row):
                return False
        
        for col in zip(*board):
            if not isValid(col):
                return False
        
        for i in range(3):
            for j in range(3):
                listOfNums = [board[x][y] for x in range(3*i,3*(i+1)) for y in range(3*j,3*(j+1))]
                if not isValid(listOfNums):
                    return False
        
        return True

                    


