#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ret = []
        count = 0
        for string in strs:
            sortedString = str(sorted(string))
            if sortedString in dic:
                ret[dic[sortedString]].append(string)
            else:      
                dic[sortedString] = count
                ret.append([string])
                count += 1
        return ret
    
            
                

