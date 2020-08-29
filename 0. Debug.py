class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
        def isScramble(self, s1: str, s2: str) -> bool:
            if len(s1) != len(s2) or sorted(s1) != sorted(s2): return False
            if len(s1) <=3:
                return True

            for i in range(1,len(s1)):
                if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])) or (self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i])):
                    return True 
            
            return False

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

print(s.isScramble("abcdefghijklmnopq","efghijklmnopqcadb"))