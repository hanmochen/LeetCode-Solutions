
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        lastPos = dummy
        pos = head
        
        while(pos is not None):
            nextPos = pos.next
            if(nextPos is not None):
                if nextPos.val == pos.val:
                    while(nextPos is not None and nextPos.val == pos.val):
                        nextPos = nextPos.next

                else:
                    lastPos.next = pos
                    lastPos = lastPos.next
                
            pos = nextPos
            
        return head



s= Solution()
nums = [1,2,3,3,4,4,5]

head = ListNode(0)
pos = head
for num in nums:
    node = ListNode(num)
    pos.next = node
    pos = pos.next

pos = head.next
while(pos):
    print(pos.val)
    pos = pos.next

s.deleteDuplicates(head.next)
pos = head
while(pos):
    print(pos.val)
    pos = pos.next
