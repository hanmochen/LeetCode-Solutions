#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        lastPos = dummy
        pos = head
        
        while(pos is not None):
            nextPos = pos.next
            if(nextPos is not None and nextPos.val == pos.val) :
                while(nextPos is not None and nextPos.val == pos.val):
                    nextPos = nextPos.next
                lastPos.next = nextPos

            else:
                lastPos.next = pos
                lastPos = pos
                
            pos = lastPos.next
                     
        return dummy.next



