#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def generateNextPosition():
            nonlocal pos_x,pos_y,direction,count,rightBound,leftBound,upBound,downBound
            if direction == 0:
                if pos_y == rightBound:
                    direction = 1
                    pos_x += 1
                    rightBound -= 1
                else:
                    pos_y += 1
            elif direction == 1:
                if pos_x == downBound:
                    direction = 2
                    pos_y -= 1
                    downBound -= 1
                else:
                    pos_x += 1
            elif direction == 2:
                if pos_y == leftBound:
                    direction = 3
                    pos_x -= 1
                    leftBound += 1
                else:
                    pos_y -= 1
            elif direction == 3:
                if pos_x == upBound:
                    direction = 0
                    pos_y += 1
                    upBound += 1
                else:
                    pos_x -= 1
            
            count += 1

    
        matrix = [n*[1] for _ in range(n) ]

        leftBound,rightBound = 0,n-1
        upBound,downBound = 1,n-1

        count = 1
        pos_x = 0
        pos_y = 0
        
        direction = 0 
        # 0 Stands for right
        # 1 Stands for down
        # 2 Stands for left
        # 3 Stands for up

        while(count <= n*n):
            matrix[pos_x][pos_y] = count
            generateNextPosition()
        
        return matrix
            

