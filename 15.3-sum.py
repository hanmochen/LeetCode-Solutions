#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(not nums): return []
        tripletSet = []
        sortedNumbers = sorted(nums)
        currentIndex = 0
        while currentIndex < len(sortedNumbers)-2 :
            currentNumber = sortedNumbers[currentIndex]
            if(currentNumber>0): return tripletSet
            leftBound = currentIndex + 1 
            rightBound = len(sortedNumbers)-1
            while(leftBound < rightBound):
                if(sortedNumbers[leftBound]+currentNumber>0): break
                sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                if(sum == 0):
                    tripletSet.append([currentNumber,sortedNumbers[leftBound],sortedNumbers[rightBound]])
                    while(sum==0 and leftBound<rightBound):
                        leftBound += 1
                        sum = currentNumber+sortedNumbers[leftBound]+sortedNumbers[rightBound]
                elif(sum > 0): rightBound -= 1
                else: leftBound += 1
            
            while(currentIndex<len(sortedNumbers)-2 and sortedNumbers[currentIndex]==currentNumber):
                currentIndex += 1
            

        return tripletSet   
                    




