#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        currentPosition = 0
        while(currentPosition < len(nums)-1):        
            oneStepRange = currentPosition +nums[currentPosition] # one step max range
            if oneStepRange >= len(nums)-1: return steps+1 # Only needs one more step
            nextPosition = oneStepRange 
            twoStepRange = oneStepRange+nums[oneStepRange]
            for i in range(currentPosition+1,oneStepRange+1):
                if i+nums[i]>twoStepRange:
                    twoStepRange = i+nums[i]
                    nextPosition = i
            steps += 1
            currentPosition = nextPosition
        
        return steps



