#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        h,w = len(board),len(board[0])
        isUsed = [[False]*w for _ in range(h)]


        def DFS(x,y,word):
            if not word: return True
            if x<0 or x>=len(board) or y<0 or y >= len(board[0]): return False
            if board[x][y] == word[0] and not isUsed[x][y]:
                word_left = word[1:]
                isUsed[x][y] = True

                if DFS(x-1,y,word_left):
                    return True
                if DFS(x+1,y,word_left):
                    return True
                if DFS(x,y-1,word_left):
                    return True
                if DFS(x,y+1,word_left):
                    return True
                
                isUsed[x][y] = False
            
            return False

        
        for i in range(h):
            for j in range(w):
                if DFS(i,j,word):
                    return True
        return False
                

