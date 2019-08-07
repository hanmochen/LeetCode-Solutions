#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
FULLSET = set('123456789')
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        vEmpty = [] # A list of empty grids
        # A list composed of sets for storing impossible value
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    vEmpty.append([i, j])
                else:
                    row[i].add(v)
                    col[j].add(v)
                    square[i//3*3+j//3].add(v)

        self.dfs(board, vEmpty, row, col, square)
                    
    def dfs(self, board, vEmpty, row, col, square):
        if len(vEmpty) == 0:
            return True

        # vPossible, the possible values list for the blank
        x, y, vPossible = None, None, ['.' for _ in range(9)] 
        # Get vPossible which has minimal length
        for v in vEmpty:
            pos = FULLSET - row[v[0]] - col[v[1]] - square[v[0]//3*3+v[1]//3]
            if len(vPossible) > len(pos):
                x, y = v
                vPossible = pos
            if len(pos) == 1:
                break

        vEmpty.remove([x, y])
        for v in vPossible:
			# Check if the value is right
            if v not in row[x] and \
            v not in col[y] and \
            v not in square[x//3*3+y//3]:
                board[x][y] = v
                row[x].add(v); col[y].add(v); square[x//3*3+y//3].add(v)
                
                # When guessed wrong value
                if not self.dfs(board, vEmpty, row, col, square):
                    board[x][y] = '.'
                    row[x].discard(v); col[y].discard(v); square[x//3*3+y//3].discard(v)
                    
                else:
                    return True
                
        else: # Do not found appropriate value
            vEmpty.append([x, y])
            return False