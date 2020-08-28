class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
                
def printList(node):
    while(node):
        print(node.val)
        node = node.next

def createList(nums):
    first = ListNode(nums[0])
    pos = first
    for i in range(1,len(nums)):
        node = ListNode(nums[i]) 
        pos.next = node
        pos = pos.next  

    return first

s = Solution()
node = createList([1])
printList(node)
x = s.partition(head=node,x=3)
printList(x)