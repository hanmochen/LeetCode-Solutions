#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        tmp = ListNode(0)
        tmp.next = head
        currPos = tmp
        idx = 1

        while(idx<m):
            idx += 1
            currPos = currPos.next

        left = currPos
        right = currPos.next
        currPos = right
        nextPos = currPos.next

        while(idx<n):

            nextPos.next,currPos,nextPos = currPos,nextPos,nextPos.next     
            idx += 1
        
        left.next = currPos
        right.next = nextPos

        return tmp.next

# @lc code=end

