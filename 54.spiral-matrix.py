#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

            
            if not matrix: return []
            answer = []
            m = len(matrix)
            n = len(matrix[0])

            leftBound = 0
            rightBound = len(matrix[0])-1
            upBound = 1
            downBound = len(matrix)-1

            count = 0

            pos_x = 0
            pos_y = 0
            direction = 0 
            
            # 0 Stands for right
            # 1 Stands for down
            # 2 Stands for left
            # 3 Stands for up

            while(count < m*n):
                answer.append(matrix[pos_x][pos_y])
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
            
            return answer
        

