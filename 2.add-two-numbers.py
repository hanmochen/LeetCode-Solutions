#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = l1
        temp = 0
        while ((l1.next is not None) or (l2.next is not None) ):
            num = l1.val + l2.val + temp
            l1.val = num % 10
            temp = num//10
            if(l1.next is None): # Make Sure l1 is longer than l2
                l1.next = l2.next
                l2.next = None
            
            l1 = l1.next
            if(l2.next is None):
                l2.val = 0
            else: l2 = l2.next  
        
        num = l1.val + l2.val + temp
        l1.val = num % 10
        temp = num//10
        if temp:
            l1.next = l2
            l2.val =1
    
        return l



