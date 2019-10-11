#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pos = head

        while(pos is not None):
            nextPos = pos.next
            while(nextPos is not None and nextPos.val == pos.val):
                nextPos = nextPos.next
            pos.next = nextPos
            pos = nextPos
        
        return head


# @lc code=end

