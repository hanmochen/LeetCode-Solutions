#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n<k or k==0: return []
        if k == 1: return [[i] for i in range(1,n+1)]
        if n==k: return [list(range(1,n+1))]
        
        return [x+[n] for x in self.combine(n-1,k-1)]+self.combine(n-1,k)

