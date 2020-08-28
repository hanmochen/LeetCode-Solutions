#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        h = len(matrix)
        w = len(matrix[0])

        dp= [w*[1] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if i == 0:
                    dp[i][j] = 1 if (matrix[i][j] == '1') else 0
                else:
                    dp[i][j] = dp[i-1][j]+1 if (matrix[i][j] == '1') else 0
        

        def largestRectangleArea(heights):
            stack = []
            heights = [0] + heights + [0]
            res = 0
            for i in range(len(heights)):
                #print(stack)
                while stack and heights[stack[-1]] > heights[i]:
                    tmp = stack.pop()
                    res = max(res, (i - stack[-1] - 1) * heights[tmp])
                stack.append(i)
            return res

            
        largestArea = 0 
        for i in range(h):
            largestArea = max(largestArea,largestRectangleArea(dp[i]))
        return largestArea
    

# @lc code=end

