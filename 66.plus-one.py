#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number = number*10 + digit
        number += 1
        answer = []
        while(number):
            answer = [number%10]+answer
            number = number//10
        return answer
        
    

