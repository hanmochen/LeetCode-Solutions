#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if(not nums): return []
        sortedNumbers = sorted(nums)
        currentIndex = 0
        currentDistance = float('inf')
        currentSum = 0
        while currentIndex < len(sortedNumbers)-2 :
            currentNumber = sortedNumbers[currentIndex]
            leftBound = currentIndex + 1 
            rightBound = len(sortedNumbers)-1
            while(leftBound < rightBound):
                sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                
                if(sum == target):
                    return target
                elif(sum > target):
                    if(sum-target<currentDistance):
                        currentDistance = sum - target
                        currentSum = sum 
                    rightBound -= 1

                else:
                    if(target-sum<currentDistance):
                        currentDistance = target-sum 
                        currentSum = sum
                    leftBound += 1
                
                print(sum) 
                print(currentDistance)

            while(currentIndex<len(sortedNumbers)-2 and sortedNumbers[currentIndex]==currentNumber):
                currentIndex += 1

        
        return currentSum
            

            
  
                    

