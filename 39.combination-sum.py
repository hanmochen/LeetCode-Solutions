#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinations(sortedCandidates,target):
            if not sortedCandidates: return []
            combinationSet = []
            largestCandidate = sortedCandidates.pop()
            count = 0
            while(target>0):
                for combination in combinations(sortedCandidates.copy(),target):
                    combinationSet.append(count*[largestCandidate]+combination)
                target -= largestCandidate
                count += 1
            if target == 0: 
                combinationSet.append(count*[largestCandidate])

            return combinationSet
        
        candidates.sort()
        return combinations(candidates,target)





