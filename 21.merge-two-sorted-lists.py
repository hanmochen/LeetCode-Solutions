#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else :
            head = l2
            l2 = l2.next

        lastPosition = head
        position1 = l1
        position2 = l2
        
        while(position1 is not None and position2 is not None):
            if(position1.val < position2.val):
                lastPosition.next = position1
                position1 = position1.next
            else:
                lastPosition.next = position2
                position2 = position2.next
            lastPosition = lastPosition.next
            
        lastPosition.next = position2 if position1 is None else position1

        return head
        


