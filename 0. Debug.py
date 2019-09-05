#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

import copy
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        if not board: return False
        h,w = len(board),len(board[0])
        isUsed = [[False]*w for _ in range(h)]


        def DFS(x,y,word,isUsed):
            if not word: return True
            if x<0 or x>=len(board) or y<0 or y >= len(board[0]): return False
            if board[x][y] == word[0] and not isUsed[x][y]:
                word_left = word[1:]
                isUsed_left = copy.deepcopy(isUsed)
                isUsed_left[x][y] = True

                return DFS(x-1,y,word_left,isUsed_left) or DFS(x+1,y,word_left,isUsed_left) or DFS(x,y+1,word_left,isUsed_left) or DFS(x,y-1,word_left,isUsed_left)
            
            return False

        
        for i in range(h):
            for j in range(w):
                if DFS(i,j,word,isUsed):
                    
                    return True
        return False
                
s= Solution()
board =[["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(s.exist(board,word))