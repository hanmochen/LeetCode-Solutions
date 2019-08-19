#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        currentPosition = 0
        while(currentPosition < len(nums)-1):        
            oneStepRange = currentPosition +nums[currentPosition] # one step max range
            if oneStepRange >= len(nums)-1: return True # Only needs one more step
            nextPosition = oneStepRange 
            twoStepRange = oneStepRange+nums[oneStepRange]
            for i in range(currentPosition+1,oneStepRange+1):
                if i+nums[i]>twoStepRange:
                    twoStepRange = i+nums[i]
                    nextPosition = i
            if nums[nextPosition] == 0: return False
            currentPosition = nextPosition
        
        return True

        

