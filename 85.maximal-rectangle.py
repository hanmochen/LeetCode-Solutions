#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        h = len(matrix)
        w = len(matrix[0])

        dp= [(w+1)*[0] for _ in range(h+1)]
        dpH = [(w+1)*[i+1] for i in range(h+1)]
        dpU = [(w+1)*[i+1] for i in range(h+1)]
        dpW = [list(range(1,w+2)) for _ in range(h+1)]
        dpL = [list(range(1,w+2)) for _ in range(h+1)]
        for i in range(h):
            for j in range(w):
                if(matrix[i][j] == '1'):
                    dpU[i+1][j+1] = dpU[i][j+1]
                    dpL[i+1][j+1] = dpL[i+1][j]
                    if i == 0 or matrix[i-1][j] == '0':
                        area = (i+2)-dpL[i+1][j+1]
                    elif j == 0 or matrix[i][j-1] == '0':
                        area = (j+2)-dpU[i+1][j+1]
                    else:
                        dpH[i+1][j+1] = max(dpH[i+1][j],dpH[i][j+1])
                        dpW[i+1][j+1] = max(dpW[i+1][j],dpW[i][j+1])
                        area = ((i+2)-dpH[i+1][j+1])*((j+2)-dpL[i+1][j+1])
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1],area)
                                  
                else:                 
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
                    
        return dp[-1][-1]



        
# @lc code=end

