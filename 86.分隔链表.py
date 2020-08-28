#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode: 
        pos = ListNode(0)
        pos.next = head
        head = pos
        while(pos.next and  pos.next.val<x):
            pos = pos.next
        curr = pos
        while(curr.next):
            if curr.next.val < x:             
                temp = curr.next
                curr.next = temp.next
                temp.next = pos.next
                pos.next = temp
                pos =  pos.next
            else:
                curr = curr.next
        return head.next

# @lc code=end

