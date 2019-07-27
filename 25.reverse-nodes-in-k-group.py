#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse_K(head: ListNode,tail: ListNode):
            previous = head.next
            point = previous.next
            head.next = tail
            previous.next = tail.next
            while(point is not tail):
                next = point.next
                point.next = previous
                previous = point
                point = next
            tail.next = previous

        if k == 1: return head
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        count = 0
        rPointer = pointer
        while(rPointer.next is not None):
            rPointer = rPointer.next
            count += 1
            if(count == k):
                count = 0
                next = pointer.next
                reverse_K(pointer,rPointer)
                rPointer = next
                pointer = rPointer
        
        return dummy.next

            

