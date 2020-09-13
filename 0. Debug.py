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
    
    def numDecodings(self, s: str) -> int:
        if s == '': return 0
        dp = [1 for i in range(len(s))]
        dp[0] = 1 if '1'<= s[0] <= '9' else 0
        for i in range(1,len(s)):
            if '1' <= s[i] <= '9':
                dp[i] = dp[i-1]+dp[i-2]  if 11 <= int(s[i-1:i+1]) <= 26 else dp[i-1]
            elif s[i] == '0' and '1'<= s[i-1] <= '2':
                dp[i] = dp[i-2]
            else: dp[i] = 0          
        return dp[-1]

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
            temp = nextPos.next
            nextPos.next = currPos
            currPos = nextPos
            nextPos = temp      
            idx += 1
        
        left.next = currPos
        right.next = nextPos

        return tmp.next
    
    def restoreIpAddresses(self, s: str) -> [str]:
        def isValid(s:str)-> bool:
            if len(s) == 1: return True
            if len(s) == 2 and s[0] != '0': return True
            if len(s) == 3 and 99 < int(s) < 256: return True
            return False
        def getIP(s:str,n:int) -> [str]:
            if n == 1: 
                return [s] if isValid(s) else []
            possibleIP = []
            for i in range(1,4):
                if (n-1) <= len(s)-i <= 3*(n-1) and isValid(s[0:i]):
                    possibleIP += [s[0:i] + '.' + ip for ip in getIP(s[i:],n-1)]
            return possibleIP
        return getIP(s,4)



            
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
print(s.restoreIpAddresses("25525511135"))
