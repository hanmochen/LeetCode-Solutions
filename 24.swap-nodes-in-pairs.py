#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        position = dummy = ListNode(0)
        dummy.next = head
        while(position.next and position.next.next):
            temp = position.next
            position.next = temp.next
            temp.next = position.next.next
            position.next.next = temp
            position = position.next.next
        return dummy.next 

        

