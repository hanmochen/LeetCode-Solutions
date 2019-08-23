#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not k: return head
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        pointer = head
        count = 0
        while(pointer is not None and count<k):
            pointer = pointer.next
            count += 1
        
        if not pointer:
            k = k%count
            return self.rotateRight(head,k)
        
        pointer2 = head
        while(pointer.next is not None):
            pointer = pointer.next
            pointer2 = pointer2.next
        dummy.next = pointer2.next
        pointer.next = head
        pointer2.next = None

        return dummy.next      

