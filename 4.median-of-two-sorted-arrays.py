#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:

        m,n = len(A),len(B)
        if(m >n):
            A,B = B,A
            m,n = len(A),len(B)
        
        if(n==0): raise ValueError
            
        high = m
        low = 0
        i = int(m+1/2)
        j = int((m+n+1)/2)-i

        while(self.atIndex(A,i-1)>self.atIndex(B,j) or self.atIndex(B,j-1)>self.atIndex(A,i)):
            if(self.atIndex(A,i-1)>self.atIndex(B,j)):
                high = i
                i = int((high+low)/2)
                j = int((m+n+1)/2)-i
            
            else:
                low = i
                i = int((high+low+1)/2)
                j = int((m+n+1)/2)-i
            

        if((m+n)%2 == 0):
            return (max(self.atIndex(A,i-1),self.atIndex(B,j-1))+min(self.atIndex(A,i),self.atIndex(B,j)))/2.0
        return max(self.atIndex(A,i-1),self.atIndex(B,j-1))

    def atIndex(self,A:List[int],index:int)-> int:
        if(index < 0): return float("-inf")
        if(index >= len(A)): return float("inf")
        return A[index]



# s = Solution()

# nums = [1,2,2,2,2,3,4]

# print(s.findLeftBound(nums,1))
# print(s.findRightBound(nums,4))


