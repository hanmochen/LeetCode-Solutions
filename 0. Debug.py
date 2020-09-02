class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def grayCode(self, n: int) -> [int]:
        if n == 0: return [0]
        nums = self.grayCode(n-1)
        nums += [num+2**(n-1) for num in nums[::-1]]    
        return nums

    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        res = [[]]
        while(nums):
            num = nums.pop(0)
            sets = [[],[num]]
            lastSet = [num]
            while(nums and nums[0] == num):              
                lastSet.append(nums.pop(0))
                sets.append(lastSet)
            res = [x+y for x in res for y in sets]
        return res
            


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


print(s.subsetsWithDup([1,2,2]))
