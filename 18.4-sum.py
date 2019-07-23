#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return []
        sortedNumbers = sorted(nums)
        firstIndex = 0
        quadSet = []
        while firstIndex < len(nums) - 3:
            firstNumber = sortedNumbers[firstIndex]
            if firstNumber*4 > target: return quadSet
            secondIndex = firstIndex + 1
            while secondIndex < len(nums) - 2:
                secondNumber = sortedNumbers[secondIndex]
                if secondNumber*3 > target - firstNumber: break
                thirdIndex = secondIndex + 1
                fourthIndex = len(nums) - 1
                while(thirdIndex < fourthIndex):
                    sum = firstNumber + secondNumber + sortedNumbers[thirdIndex] + sortedNumbers[fourthIndex]
                    if (sum > target): fourthIndex -= 1
                    elif (sum < target): thirdIndex += 1
                    else: 
                        quadSet.append([firstNumber,secondNumber,sortedNumbers[thirdIndex],sortedNumbers[fourthIndex]])
                        while( thirdIndex < fourthIndex and firstNumber + secondNumber + sortedNumbers[thirdIndex] + sortedNumbers[fourthIndex] == target ):
                            thirdIndex += 1
                while(secondIndex < len(nums) - 2 and sortedNumbers[secondIndex] == secondNumber ):
                    secondIndex += 1
            while(firstIndex < len(nums)-3 and sortedNumbers[firstIndex] == firstNumber):
                firstIndex += 1

        return quadSet


         
            

