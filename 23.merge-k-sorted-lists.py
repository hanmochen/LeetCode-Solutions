#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        dummy = pointer = ListNode(0)
        priorityQueue = PriorityQueue()
        count = 0
        for l in lists:
            if l:
                priorityQueue.put((l.val, count,l))
                count += 1
        while not priorityQueue.empty():
            val,_,node = priorityQueue.get()
            pointer.next = ListNode(val)
            pointer = pointer.next
            node = node.next
            if node:
                priorityQueue.put((node.val,count,node))
                count += 1 
        return dummy.next
        

