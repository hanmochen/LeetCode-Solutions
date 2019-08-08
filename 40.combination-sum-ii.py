#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinations(sortedCandidates,target):
            if not sortedCandidates: return []
            combinationSet = []
            smallestCandidate = sortedCandidates.pop(0)
            if smallestCandidate>target : return []
            if smallestCandidate == target: return [[smallestCandidate]]
    
            for combination in combinations(sortedCandidates.copy(),target-smallestCandidate):
                combinationSet.append([smallestCandidate]+combination)
            
            while(sortedCandidates and sortedCandidates[0] == smallestCandidate):
                sortedCandidates.pop(0)
            combinationSet += combinations(sortedCandidates,target)
            return combinationSet
        
        candidates.sort()
        return combinations(candidates,target)

